# theme.py
# This file contains some definitions and functions to make PHCtool more themeable in the future.
# This is an early version - more will follow.
#


##some generic file definitions
phc_icon_22 = "inc/phc_icon_22.png"
phc_exit_22 = "inc/phc_exit_22.png"
sidelogo = "inc/sideimage.png"
helplogo = "inc/helplogo.png"



##some color definitions






#################################
##    nothing to change here   ##
#################################
import gtk

def start_theme(wtree):
#
#
#
		wtree.get_widget("eventbox_bottom").modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("black"))
		wtree.get_widget("label_ProcHardCtl").modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse("lightblue"))
