#!/usr/bin/env python

import sys, time, os
sys.path.append('inc')			##search our subdir for librarys

try:
	import pygtk, gobject
	#tell pyGTK, if possible, that we want GTKv2
	pygtk.require("2.0")
except:
	#Some distributions come with GTK2, but not pyGTK
	print "pyGTK missed"
	pass
try:
  	import gtk
 	import gtk.glade
except:
  	print "You need to install pyGTK or GTKv2 ",
  	print "or set your PYTHONPATH correctly."
  	print "try: export PYTHONPATH=",
  	print "/usr/local/lib/python2.2/site-packages/"
  	sys.exit(1)
	#now we have both gtk and gtk.glade imported
	#Also, we know we are running GTK v2
try:
  	import phctool_globals as pglobals
except:
  	print "phctool globals missing or corrupted"
  	sys.exit(1)

class appgui:
	def __init__(self, topic):
		gladefile="inc/phctoolhelp.glade";			##get glade file
		windowname="phctoolhelp";				##define window name
		self.wTree=gtk.glade.XML (gladefile,windowname);	##get applets tree
		self.textbuff=gtk.TextBuffer(None);			##text buffer
		self.topic = topic					##the topic we want to show some help about
		##read certain helpfile and display its content
		self.textbuff.set_text(self.load_help_file());
		self.wTree.get_widget("textview").set_buffer(self.textbuff);
		#Get the Main Window, and connect the "destroy" event
		self.window = self.wTree.get_widget("MainWindow")
		if (self.window):
			self.window.connect("destroy", self.quit)
		##If the Textfield is clicked the popup gets closed
		self.wTree.get_widget("textview").connect("button_press_event", self.quit)
		###define events and its handlers
		dic = {	"destroy" :self.quit } 
      		self.wTree.signal_autoconnect(dic)
		return

	def load_help_file(self):
		if os.path.exists(sys.path[0]+"/inc/textfiles/"+self.topic+".inc"):
			helpfile = file(sys.path[0]+"/inc/textfiles/"+self.topic+".inc");
			text="";
        		for line in helpfile:
				text += line
        		helpfile.close()
		else:
			text = "helpfile not found"
  		return text

#####event handlers#########
	def quit(self, *args):
	##quit program
		self.wTree.get_widget("phctoolhelp").destroy()


def popup(topicnr):
	if len(str(topicnr))==1:
		if topicnr == 0:
			param = "popup_info"
		elif topicnr == 1:
			param = "popup_vids"
		elif topicnr == 2:
			param = "popup_throttle"
		elif topicnr == 3:
			param = "popup_settings"
		elif topicnr == 4:
			param = "popup_analysis"
		else:	##default
			param = "popup_about"

		app=appgui(param)
		gtk.main()

