#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# License: GPLv2

import argparse
import gtk
from gtk import gdk
import cairo
import gobject
import subprocess

import psutil

def normalize_color_hex(s):
  if s[0] == "#":
    s = s[1:]
  if len(s) == 3:
    s = s[0] + s[0] + s[1] + s[1] + s[2] + s[2]
  if len(s) == 4:
    s = s[0] + s[0] + s[1] + s[1] + s[2] + s[2] + s[3] + s[3]
  if len(s) == 6:
    s += "ff"
  assert(len(s) == 8)
  return s

def color_hex_to_float(s):
  s = normalize_color_hex(s)
  return [int(s[0:2], 16)/255.0, int(s[2:4], 16)/255.0, int(s[4:6], 16)/255.0, int(s[6:8], 16)/255.0]

def color_hex_to_int(s):
  s = normalize_color_hex(s)
  return int(s, 16)

def bytes2human(n):
  # http://code.activestate.com/recipes/578019
  # >>> bytes2human(10000)
  # '9.8 K'
  # >>> bytes2human(100001221)
  # '95.4 M'
  symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
  prefix = {}
  for i, s in enumerate(symbols):
    prefix[s] = 1 << (i + 1) * 10
  for s in reversed(symbols):
    if n >= prefix[s]:
      value = float(n) / prefix[s]
      return '%.1f %sB' % (value, s)
  return "%s B" % n


# Parameters
parser = argparse.ArgumentParser()
parser.add_argument("--cpu", help="Show a CPU activity graph", dest="cpu", action="store_true")
parser.add_argument("--core", help="Show a CPU activity graph for each logical CPU core", dest="core", action="store_true")
parser.add_argument("--mem", help="Show a memory usage graph", dest="mem", action="store_true")
parser.add_argument("--mem_percent", help="Tooltip: Show used memory in percentage", dest="mem_percent", action="store_true")
parser.add_argument("--swap", help="Show a swap usage graph", dest="swap", action="store_true")
parser.add_argument("--swap_percent", help="Tooltip: Show used swap in percentage", dest="swap_percent", action="store_true")
parser.add_argument("--net", help="Show a network usage graph", dest="net", action="store_true")
parser.add_argument("--net_scale", help="Maximum value for the network usage graph, in Mbps. Default: 40.", default=40, type=int)
parser.add_argument("--io", help="Show a disk I/O graph", dest="io", action="store_true")
parser.add_argument("--io_scale", help="Maximum value for the disk I/O graph, in MB/s. Default: 100.", default=100, type=int)

parser.add_argument("--size", help="Icon size in pixels. Default: 22.", default=22, type=int)
parser.add_argument("--invert", help="Try to invert order of icons ( might not work as it depends highly on the system tray used )", dest="invert", action="store_true")
parser.add_argument("--interval", help="Refresh interval in miliseconds. Default: 1000 (1sec).", default=1000, type=int)
parser.add_argument("--bg", help="Background color (RGBA hex). Default: #00000077.", default="#00000077")
parser.add_argument("--fg_cpu", help="CPU graph color (RGBA hex). Default: #3f3.", default="#3f3")
parser.add_argument("--fg_mem", help="Memory graph color (RGBA hex). Default: #ff3.", default="#ff3")
parser.add_argument("--fg_swap", help="Swap graph color (RGBA hex). Default: #419CFF.", default="#419CFF")
parser.add_argument("--fg_net", help="Network graph color (RGBA hex). Default: #33f.", default="#33f")
parser.add_argument("--fg_io", help="Disk I/O graph color (RGBA hex). Default: #3cf.", default="#3cf")

parser.add_argument("--task_manager", help="Task manager to execute on left click. Default: None.")

parser.set_defaults(cpu=False)
parser.set_defaults(core=False)
parser.set_defaults(mem=False)
parser.set_defaults(swap=False)
parser.set_defaults(net=False)
parser.set_defaults(io=False)
args = parser.parse_args()

w = h = args.size
invert = args.invert
interval = args.interval
bgCol = color_hex_to_int(args.bg)
fgCpu = color_hex_to_float(args.fg_cpu)
fgRam = color_hex_to_float(args.fg_mem)
fgSwap = color_hex_to_float(args.fg_swap)
fgNet = color_hex_to_float(args.fg_net)
fgDiskIo = color_hex_to_float(args.fg_io)

cpuEnabled = args.cpu or args.core
mergeCpus = not args.core
ramEnabled = args.mem
memPercent = args.mem_percent
swapEnabled = args.swap
swapPercent = args.swap_percent
netEnabled = args.net
netScale = args.net_scale
diskIoEnabled = args.io
diskIoScale = args.io_scale
taskMgr = args.task_manager

if not cpuEnabled and not ramEnabled and not swapEnabled and not netEnabled and not diskIoEnabled:
  cpuEnabled = mergeCpus = ramEnabled = swapEnabled = netEnabled = diskIoEnabled = True

class HardwareMonitor:
  def __init__(self):
    if invert:
      self.initDiskIo()
      self.initNet()
      self.initSwap()
      self.initRam()
      self.initCpus()
      self.drawDiskIo()
      self.drawNet()
      self.drawSwap()
      self.drawRam()
      self.drawCpus()
    else:
      self.initCpus()
      self.initRam()
      self.initSwap()
      self.initNet()
      self.initDiskIo()
      self.drawCpus()
      self.drawRam()
      self.drawSwap()
      self.drawNet()
      self.drawDiskIo()
    gobject.timeout_add(interval, self.update)

  def rightClickEvent(self, icon, button, time):
    menu = gtk.Menu()
    quit = gtk.MenuItem("Quit")
    quit.connect("activate", gtk.main_quit)
    menu.append(quit)
    menu.show_all()
    menu.popup(None, None, gtk.status_icon_position_menu, button, time, icon)

  def leftClickEvent (self, icon):
    if not taskMgr:
      return
    subprocess.Popen(taskMgr)

  def initCpus(self):
    if not cpuEnabled:
      return
    if mergeCpus:
      self.cpus = [[0 for x in range(w)]]
      psutil.cpu_percent(percpu=mergeCpus)
    else:
      self.cpus = [[0 for x in range(w)] for c in range(len(psutil.cpu_percent(percpu=not mergeCpus)))]
    self.cpuIcons = [gtk.StatusIcon() for c in range(len(self.cpus))]
    for c in range(len(self.cpus)):
      self.cpuIcons[c].set_title("hwmon 1 cpu{0}".format("" if mergeCpus else (" " + str(c+1))))
      self.cpuIcons[c].connect("popup-menu", self.rightClickEvent)
      self.cpuIcons[c].connect("activate", self.leftClickEvent)
      self.cpuIcons[c].set_visible(True)

  def updateCpus(self):
    if not cpuEnabled:
      return
    vals = psutil.cpu_percent(percpu=not mergeCpus)
    if mergeCpus:
      vals = [vals]
    for c in range(len(vals)):
      self.cpus[c].append(vals[c])
      self.cpus[c].pop(0)
      self.cpuIcons[c].set_tooltip_text("CPU{0}: {1}%".format("" if mergeCpus else (" " + str(c+1)), vals[c]))

  def drawCpus(self):
    if not cpuEnabled:
      return
    for c in range(len(self.cpus)):
      self.draw(self.cpus[c], self.cpuIcons[c], bgCol, fgCpu)


  def initRam(self):
    if not ramEnabled:
      return
    self.ram = [0 for x in range(w)]
    self.ramIcon = gtk.StatusIcon()
    self.ramIcon.set_title("hwmon 2 memory")
    self.ramIcon.connect("popup-menu", self.rightClickEvent)
    self.ramIcon.connect("activate", self.leftClickEvent)
    self.ramIcon.set_visible(True)

  def updateRam(self):
    if not ramEnabled:
      return
    mem = psutil.virtual_memory()
    total = mem[0]
    used = mem[3]
    used_percent = mem[2]
    self.ram.append(used_percent)
    self.ram.pop(0)
    if memPercent:
      self.ramIcon.set_tooltip_text("Memory: %d%% used of %s" % (used_percent, bytes2human(total)))
    else:
      self.ramIcon.set_tooltip_text("Memory: %s used of %s" % (bytes2human(used), bytes2human(total)))

  def drawRam(self):
    if not ramEnabled:
      return
    self.draw(self.ram, self.ramIcon, bgCol, fgRam)

  def initSwap(self):
    if not swapEnabled:
      return
    self.swap = [0 for x in range(w)]
    self.swapIcon = gtk.StatusIcon()
    self.swapIcon.set_title("hwmon 3 swap")
    self.swapIcon.connect("popup-menu", self.rightClickEvent)
    self.swapIcon.connect("activate", self.leftClickEvent)

  def updateSwap(self):
    if not swapEnabled:
      return
    swap = psutil.swap_memory()
    total = swap[0]
    used = swap[1]
    used_percent = swap[3]
    if bool(self.swapIcon.get_visible()) != bool(total):
      self.swapIcon.set_visible(total)
    self.swap.append(used_percent)
    self.swap.pop(0)
    if swapPercent:
      self.swapIcon.set_tooltip_text("Swap: %d%% used of %s" % (used_percent, bytes2human(total)))
    else:
      self.swapIcon.set_tooltip_text("Swap: %s used of %s" % (bytes2human(used), bytes2human(total)))

  def drawSwap(self):
    if not swapEnabled:
      return
    self.draw(self.swap, self.swapIcon, bgCol, fgSwap)

  def initNet(self):
    if not netEnabled:
      return
    self.net = [0 for x in range(w)]
    v = psutil.net_io_counters(pernic=False)
    self.netBytes = v[0] + v[1]
    self.netIcon = gtk.StatusIcon()
    self.netIcon.set_title("hwmon 4 network")
    self.netIcon.connect("popup-menu", self.rightClickEvent)
    self.netIcon.connect("activate", self.leftClickEvent)
    self.netIcon.set_visible(True)

  def updateNet(self):
    if not netEnabled:
      return
    v = psutil.net_io_counters(pernic=False)
    v = v[0] + v[1]
    delta = v - self.netBytes
    self.netBytes = v
    self.net.append(delta * 8 / 1.0e6)
    self.net.pop(0)
    self.netIcon.set_tooltip_text("Network: %.1f Mb/s" % (delta * 8 / 1.0e6))

  def drawNet(self):
    if not netEnabled:
      return
    self.draw(self.net, self.netIcon, bgCol, fgNet, netScale)


  def initDiskIo(self):
    if not diskIoEnabled:
      return
    self.diskIo = [0 for x in range(w)]
    v = psutil.disk_io_counters(perdisk=False)
    self.diskIoBytes = v[2] + v[3]
    self.diskIoIcon = gtk.StatusIcon()
    self.diskIoIcon.set_title("hwmon 5 disk i/o")
    self.diskIoIcon.connect("popup-menu", self.rightClickEvent)
    self.diskIoIcon.connect("activate", self.leftClickEvent)
    self.diskIoIcon.set_visible(True)

  def updateDiskIo(self):
    if not diskIoEnabled:
      return
    v = psutil.disk_io_counters(perdisk=False)
    v = v[2] + v[3]
    delta = v - self.diskIoBytes
    self.diskIoBytes = v
    self.diskIo.append(delta / 1.0e6 / 10)
    self.diskIo.pop(0)
    partitions = psutil.disk_partitions(all=False)
    strPartitions = ""
    for part in psutil.disk_partitions(all=False):
      if 'cdrom' in part.opts or part.fstype == '':
        continue
      usage = psutil.disk_usage(part.mountpoint)
      strPartitions += "\n%s %d%% of %s (%s)" % (part.mountpoint, int(usage.percent), bytes2human(usage.total), part.fstype)
    self.diskIoIcon.set_tooltip_text("Disk I/O: %.1f MB/s\n%s" % (delta / 1.0e6 / 10, strPartitions))

  def drawDiskIo(self):
    if not diskIoEnabled:
      return
    self.draw(self.diskIo, self.diskIoIcon, bgCol, fgDiskIo, diskIoScale)


  def draw(self, graph, icon, bgCol, fgCol, max=100):
    bg = gdk.Pixbuf(gdk.COLORSPACE_RGB, True, 8, w, h)
    bg.fill(bgCol)
    pixbuf = gdk.Pixbuf(gdk.COLORSPACE_RGB, True, 8, w, h)
    pixbuf.fill(0x00000000)
    pixmap = pixbuf.render_pixmap_and_mask(alpha_threshold=127)[0]
    cr = pixmap.cairo_create()
    cr.set_source_rgba(fgCol[0], fgCol[1], fgCol[2], fgCol[3])
    for x in range(w):
      y = int(round(graph[x]/max * h))
      if y:
        cr.move_to(x, h)
        cr.line_to(x, h - y)
    cr.stroke()
    pixbuf.get_from_drawable(pixmap, pixmap.get_colormap(), 0, 0, 0, 0, w, h)
    pixbuf = pixbuf.add_alpha(True, 0x00, 0x00, 0x00)
    pixbuf.composite(bg, 0, 0, w, h, 0, 0, 1, 1, gtk.gdk.INTERP_NEAREST, 255)
    icon.set_from_pixbuf(bg)


  def update(self):
    self.updateCpus()
    self.updateRam()
    self.updateSwap()
    self.updateNet()
    self.updateDiskIo()
    self.drawCpus()
    self.drawRam()
    self.drawSwap()
    self.drawNet()
    self.drawDiskIo()
    return True


if __name__ == '__main__':
  HardwareMonitor()
  gtk.main()