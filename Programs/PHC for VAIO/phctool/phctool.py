#!/usr/bin/env python

import sys, time
sys.path.append('inc')			##search our subdir for librarys
sys.path.append('inc/libs')		##also search this subdir for librarys

###################################################
try:
	import pygtk, gobject
	#tell pyGTK, if possible, that we want GTKv2
	pygtk.require("2.0")
except:
	#Some distributions come with GTK2, but not pyGTK
	print "pyGTK missed"
	pass
###################################################
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
###################################################
try:
  	import generic
except:
  	print "generic function library missing or corrupted"
  	sys.exit(1)
###################################################
try:
  	import msr
except:
  	print "msr function library missing or corrupted"
  	sys.exit(1)
###################################################
try:
  	import throttling
except:
  	print "throttling function library missing or corrupted"
  	sys.exit(1)
###################################################
try:
  	import cpuinfo
except:
  	print "cpuinfo function library missing or corrupted"
  	sys.exit(1)
###################################################
try:
  	import voltages
except:
  	print "voltage calculation library missing or corrupted"
  	sys.exit(1)
###################################################
try:
  	import phctool_globals as pglobals
except:
  	print "phctool globals missing or corrupted"
  	sys.exit(1)
###################################################
try:
  	import phctoolhelp
except:
  	print "phctoolhelp modul missing or corrupted"
  	sys.exit(1)
###################################################
try:
  	import theme
except:
  	print "theme modul missing or corrupted"
  	sys.exit(1)
###################################################

class appgui:
	def __init__(self):
		self.phcdata=generic.phc(self)				##functions for PHC
		self.cpuinfo=cpuinfo.cpuinfo()				##functions to gather CPU informations
		self.msrinfo=msr.msr_interface()			##functions for MSR (to check if values are assigned)
		self.throttling=throttling.throttlecontrol(self.cpuinfo.data)
		self.voltages=voltages.voltage(self.cpuinfo.data)
		self.data = self.cpuinfo.data
		gladefile="inc/phctool.glade";				##get glade file
		windowname="phctool";					##define window name
		self.wTree=gtk.glade.XML(fname=gladefile, root=windowname)		##get applets tree

		###set window title, Version and icons
		self.wTree.get_widget("phctool").set_title(pglobals.name+" V"+pglobals.version);
		self.wTree.get_widget("label_ProcHardCtl").set_text(pglobals.name+" V"+pglobals.version);

		#Get the Main Window, and connect the "destroy" event
		self.window = self.wTree.get_widget("MainWindow")
		if (self.window):
			self.window.connect("destroy", self.quit)

		###do some actions to get data, etc
		self.phcdata.RestoreValues()		##restore VIDs from last session		
		self.ShowCPUInfos()			##display CPU informations
		self.ShowPHCVIDs()			##display current VIDs
		self.ShowThrottlingControl()		##display trottling Controls
		self.ShowStoreSettings()		##display settings about what values shall be reloaded
		self.ShowMSRAnalysis()			##display VIDs analysis Tab
		self.ReadAboutFile()
		###define events and its handlers
		dic = { "on_button_save_clicked" :	self.on_button_save_clicked, 
			"on_button_restore_clicked" :	self.on_button_restore_clicked,
			"clicked_restoreopts" :		self.clicked_restoreopts, 
			"on_button_msrrefresh" : 	self.on_button_msrrefresh,
			"help_button_clicked" : 	self.display_help_popup,
			"destroy" :			self.quit 
			} 
      		self.wTree.signal_autoconnect(dic)
		theme.start_theme(self.wTree)		##start the theming of PHCtool (e.g. setting colors, etc)
		return

	def ReadAboutFile(self):
	##read the file's content and return it
		abuff=gtk.TextBuffer(None);
        	about = file(sys.path[0]+"/inc/textfiles/about.inc");
		text="";
        	for line in about:
			text += line
        	about.close()
		###set buffer to textview
		abuff.set_text(text);
		self.wTree.get_widget("textview_aboutphctool").set_buffer(abuff);

	def ShowStoreSettings(self):
	##get RestoreOpts and affinate them to the checkboxes
		if "V" in self.phcdata.storeopts:
			self.wTree.get_widget("checkbutton_reloadvids").set_active(True)
		if "T" in self.phcdata.storeopts:
			self.wTree.get_widget("checkbutton_reloadthrottles").set_active(True)


	def ShowCPUInfos(self):
	##display collected data
		notebook = self.wTree.get_widget("cpuinfo_notebook")							##get the notebook where we want to add cpu infos	
		for cpu in self.data:
			##create the components we need for each Tab / each CPUinfo
			setattr(self,"scrollwindow"+str(cpu),gtk.ScrolledWindow())					##create scrolled window
			setattr(self,"treeview"+str(cpu),gtk.TreeView())						##create TreeView
			setattr(self,"tab_hbox"+str(cpu),gtk.HBox())							##create tab hbox
			setattr(self,"tab_label"+str(cpu),gtk.Label("CPU"+str(cpu)))					##create tab label
			setattr(self,"tab_image"+str(cpu),gtk.Image())							##create tab image
			setattr(self,"liststore"+str(cpu),gtk.ListStore(str, str, str, 'gboolean'))			##create liststore object
			setattr(self,"tvcolumn0"+str(cpu),gtk.TreeViewColumn('Attributes'))				##create first column
			setattr(self,"tvcolumn1"+str(cpu),gtk.TreeViewColumn('Values'))					##create second column
			setattr(self,"cell0"+str(cpu),gtk.CellRendererText())						##create cell-renderer 0
			setattr(self,"cell1"+str(cpu),gtk.CellRendererText())						##create cell-renderer 1

			##define properties of the components
			getattr(self,"tab_image"+str(cpu)).set_from_file(theme.phc_icon_22)				##insert generic PHClogo
			getattr(self,"scrollwindow"+str(cpu)).set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)	##define when scrollbars are visible
			getattr(self,"cell0"+str(cpu)).set_property('cell-background', 'grey')				##cell0 background color
			getattr(self,"cell1"+str(cpu)).set_property('cell-background', 'white')				##cell1 background color

			##now assembly the components
			getattr(self,"tab_hbox"+str(cpu)).add(getattr(self,"tab_image"+str(cpu)))			##add image to the hbox
			getattr(self,"tab_hbox"+str(cpu)).add(getattr(self,"tab_label"+str(cpu)))			##add label to the hbox
			getattr(self,"treeview"+str(cpu)).append_column(getattr(self,"tvcolumn0"+str(cpu)))		##append column0 to TreeView
			getattr(self,"treeview"+str(cpu)).append_column(getattr(self,"tvcolumn1"+str(cpu)))		##append column1 to TreeView
			getattr(self,"scrollwindow"+str(cpu)).add(getattr(self,"treeview"+str(cpu)))			##add treeview to ScrolledWindow
			notebook.append_page(getattr(self,"scrollwindow"+str(cpu)),getattr(self,"tab_hbox"+str(cpu)))	##add ScrolledWindow and HBox 
			
			## now we generate the data to display. 
			## we'll make some informations more readable to human users, etc

			##gernerate information about available throttling states##
			self.throttling.data[cpu]['exist'] = False
			if self.throttling.data[cpu]['exist']:
				count =self.throttling.data[cpu]['state_count']
				firststate = self.throttling.data[cpu]['states']['T0'];
				laststate = self.throttling.data[cpu]['states']['T'+str(count-1)]
				throttlestring=str(count)+" states available (from "+ firststate +'% to ' + laststate+'%)'
			else:
				throttlestring="not available"

			##generate Model string
			modelstring = "Vendor:"+self.data[cpu]["modelid"]["vendor_id"]		##vendor id
			modelstring += ", Family:"+self.data[cpu]["modelid"]["family"]		##family id
			modelstring += ", Model:"+self.data[cpu]["modelid"]["model"]		##model id
			modelstring += ", Stepping:"+self.data[cpu]["modelid"]["stepping"]	##stepping id


			##generate PHC String
			if self.cpuinfo.cpu_have_phc(cpu):
				phcstring="available"
				phcversion=self.cpuinfo.phc_version(cpu)
			else:
				phcstring="missing"
				phcversion=""

			##generate MSR String
			if self.msrinfo.cpu_have_msr(cpu):
				msrstring="available"
			else:
				msrstring="not available"

			##generate Freq String
			if self.data[cpu]['stepping']:
				freqstring=""
				for speedstep in self.data[cpu]['frequencies']:

					freqstring+=str(int(speedstep)/1000)+"Mhz "
			else:
				freqstring ="not available"

			##generate Voltage calculation formula availability string
			##generate MSR String
			if self.data[cpu]['voltages']['formula']['available']:
				formstring="CPU recognized, calculation available"
			else:
				formstring="CPU not recognized - calculation not available"

			###########################################################
			##display formatted data	
			getattr(self,"liststore"+str(cpu)).append(["Name", 0, self.data[cpu]["model"], True])
			getattr(self,"liststore"+str(cpu)).append(["CPU Model ", 0, modelstring, True])	
			getattr(self,"liststore"+str(cpu)).append(["Frequencies", 0, freqstring, True])
			getattr(self,"liststore"+str(cpu)).append(["Throttling", 0, throttlestring, True])
			getattr(self,"liststore"+str(cpu)).append(["PHC extensions", 0, phcstring, True])
			getattr(self,"liststore"+str(cpu)).append(["PHC version", 0, phcversion, True])
			getattr(self,"liststore"+str(cpu)).append(["MSR extensions", 0, msrstring, True])
			getattr(self,"liststore"+str(cpu)).append(["Vcc calculation", 0, formstring, True])

			getattr(self,"treeview"+str(cpu)).set_model(getattr(self,"liststore"+str(cpu)))			##

        		# add the cells to the columns
        		getattr(self,"tvcolumn0"+str(cpu)).pack_start(getattr(self,"cell0"+str(cpu)), True)
        		getattr(self,"tvcolumn1"+str(cpu)).pack_start(getattr(self,"cell1"+str(cpu)), True)
        		# set the cell attributes to the appropriate liststore column
        		# GTK+ 2.0 doesn't support the "stock_id" property
        		getattr(self,"tvcolumn0"+str(cpu)).set_attributes(getattr(self,"cell0"+str(cpu)), text=0)
        		getattr(self,"tvcolumn1"+str(cpu)).set_attributes(getattr(self,"cell1"+str(cpu)), text=2, cell_background_set=3)

			getattr(self,"tab_hbox"+str(cpu)).show_all()							##show tab image and label
			notebook.show_all()										##show contents of the notebook



	def ShowThrottlingControl(self):
	##Show Throttling Tab and content
		table = self.wTree.get_widget("table_throttle")							##create a table object
		table.resize(len(self.data),3) 									## rows = cpu's, cols =3 (label_CPUname, VScale, label_Percentage)
		for cpu in self.data:
		    if self.throttling.data[cpu]['exist']:
			setattr(self, 'label_CPUnr'+str(cpu), gtk.Label("CPU "+str(cpu))) 			##create label
			setattr(self, 'label_TState'+str(cpu), gtk.Label(" / "))				##create label
			adj = gtk.Adjustment(lower=0, upper=7, step_incr=1)  					##adjustment for VScale
			setattr(self, 'vscale'+str(cpu), gtk.VScale(adj)) 					##create VScale

			getattr(self, 'vscale'+str(cpu)).set_digits(0)						##set Zero digets
			tid = self.throttling.data[cpu]['active_state']						##throttling id
			getattr(self, 'vscale'+str(cpu)).set_value(tid)						##display throttling id
			getattr(self, 'label_TState'+str(cpu)).set_text(self.throttling.data[cpu]['states']['T'+str(tid)]+"%")

			table.attach(getattr(self,'label_CPUnr'+str(cpu)),0+int(cpu),1+int(cpu),0,1)		#child, left_attach, right_attach, top_attach, bottom_attach
			table.attach(getattr(self,'vscale'+str(cpu)),0+int(cpu),1+int(cpu),1,2) 		#child, left_attach, right_attach, top_attach, bottom_attach
			table.attach(getattr(self,'label_TState'+str(cpu)),0+int(cpu),1+int(cpu),2,3) 		#child, left_attach, right_attach, top_attach, bottom_attach
			getattr(self, 'vscale'+str(cpu)).connect("value_changed", self.On_Change_Throttle_Scale, str(cpu))

			getattr(self, 'vscale'+str(cpu)).set_name("vscale"+str(cpu))
			getattr(self, 'label_CPUnr'+str(cpu)).show()
			getattr(self, 'vscale'+str(cpu)).show()
			getattr(self, 'label_TState'+str(cpu)).show()


	def RefreshThrottleControls(self):
	##reads the actual throttling-state from cpuinfos and adjusts the vscale's
		for cpu in self.data:
			tid = self.throttling.data[cpu]['active_state']
			getattr(self, 'vscale'+str(cpu)).set_value(tid)



	def ShowPHCVIDs(self):
		notebook = self.wTree.get_widget("voltages_notebook")
		for cpu in self.data:
			columns = self.data[cpu]['frequencies']								##define the amount of columns we'll use to display all data
			##create the components we need for each Tab
			setattr(self,"tab_hbox"+str(cpu),gtk.HBox())								##create tab hbox
			setattr(self,"tab_label"+str(cpu),gtk.Label("CPU"+str(cpu)))						##create tab label
			setattr(self,"tab_image"+str(cpu),gtk.Image())								##create tab image
			setattr(self,"voltage_table"+str(cpu),gtk.Table(rows=len(columns)+1, columns=4))								##create tab hbox
			##set attributes
			getattr(self,"tab_image"+str(cpu)).set_from_file(theme.phc_icon_22)					##insert generic PHClogo
			##now assembly the components
			getattr(self,"tab_hbox"+str(cpu)).add(getattr(self,"tab_image"+str(cpu)))				##add image to the hbox
			getattr(self,"tab_hbox"+str(cpu)).add(getattr(self,"tab_label"+str(cpu)))				##add label to the hbox
			notebook.append_page(getattr(self,"voltage_table"+str(cpu)),getattr(self,"tab_hbox"+str(cpu)))		##add ScrolledWindow and HBox 

			setattr(self,"voltage_vidlabel"+str(cpu),gtk.Label("new\nVID:"))					##create label
			getattr(self,"voltage_vidlabel"+str(cpu)).set_alignment(0.10, 0.10)					##set label alignment
			getattr(self,"voltage_table"+str(cpu)).attach(getattr(self,"voltage_vidlabel"+str(cpu)),0,1,1,2)	##attach label to table

			setattr(self,"voltage_voltlabel"+str(cpu),gtk.Label("new\nVoltage:"))
			getattr(self,"voltage_voltlabel"+str(cpu)).set_alignment(0.10, 0.10)
			getattr(self,"voltage_table"+str(cpu)).attach(getattr(self,"voltage_voltlabel"+str(cpu)),0,1,2,3)

			setattr(self,"voltage_difflabel"+str(cpu),gtk.Label("difference to\noriginal:"))
			getattr(self,"voltage_difflabel"+str(cpu)).set_alignment(0.10, 0.10)
			getattr(self,"voltage_table"+str(cpu)).attach(getattr(self,"voltage_difflabel"+str(cpu)),0,1,3,4)

			if self.data[cpu]["phc"]:
				for col in range(len(columns)):
				#create widgets and set properties for each speedstep
				#the processor can run on
					setattr(self,"voltage_freqlabel"+str(cpu)+"_"+str(col),gtk.Label(str(int(columns[col]) / 1000)+"Mhz"))
					getattr(self,"voltage_table"+str(cpu)).attach(getattr(self,"voltage_freqlabel"+str(cpu)+"_"+str(col)),1+col,2+col,0,1)
	
					adj = gtk.Adjustment(lower=0, upper=float(self.data[cpu]["phcdefaultvalues"][col]), step_incr=1)	##adjustment for SpinButton:sthe lowest is 0, the highest one is the default VID of that speedstep
	
					setattr(self, 'spinbtn'+str(cpu)+str(col), gtk.SpinButton(adj,0.0,0)) 					##create SpinButton
					getattr(self, 'spinbtn'+str(cpu)+str(col)).set_value(int(self.data[cpu]["phcvalues"][col]))		##set SpinButton initial value
					getattr(self, 'spinbtn'+str(cpu)+str(col)).set_width_chars(2)						##set char width
					getattr(self, 'spinbtn'+str(cpu)+str(col)).connect("changed", self.on_vid_spinbutton_change, str(cpu), col)	#connect woth event
					getattr(self,"voltage_table"+str(cpu)).attach(getattr(self, 'spinbtn'+str(cpu)+str(col)),1+col,2+col,1,2,gtk.EXPAND)
	
					setattr(self,"voltage_volttext"+str(cpu)+"_"+str(col),gtk.Entry())
					getattr(self,"voltage_volttext"+str(cpu)+"_"+str(col)).set_width_chars(6)
					getattr(self,"voltage_volttext"+str(cpu)+"_"+str(col)).set_editable(False)
					getattr(self,"voltage_table"+str(cpu)).attach(getattr(self,"voltage_volttext"+str(cpu)+"_"+str(col)),1+col,2+col,2,3,gtk.EXPAND)
	
					setattr(self,"voltage_difftext"+str(cpu)+"_"+str(col),gtk.Entry())
					getattr(self,"voltage_difftext"+str(cpu)+"_"+str(col)).set_width_chars(6)
					getattr(self,"voltage_difftext"+str(cpu)+"_"+str(col)).set_editable(False)
					getattr(self,"voltage_table"+str(cpu)).attach(getattr(self,"voltage_difftext"+str(cpu)+"_"+str(col)),1+col,2+col,3,4,gtk.EXPAND)
	
					##call the event handler to write initial data to each textfield
					self.on_vid_spinbutton_change(getattr(self, 'spinbtn'+str(cpu)+str(col)) ,str(cpu), col)
	
			getattr(self,"tab_hbox"+str(cpu)).show_all()
			notebook.show_all()


	def ShowMSRAnalysis(self):
	###this will initially generate the Tab to analyse current VIDs the CPU runs with
		columns = {0:'CPU', 1:'target VID', 2:'target Vcc', 3:'reached VID', 4:'reached Vcc'}						##define the amount of columns we'll use to display all data
		analyse_treeview = self.wTree.get_widget("analyse_vids_treeview")		 
		setattr(self,"analyse_liststore",gtk.ListStore(str, str, str, str, str))					##create liststore object

		for col in columns:
			setattr(self,"analyse_tvcolumn"+str(col),gtk.TreeViewColumn(columns[col]))				##create a column
			setattr(self,"analyse_cell"+str(col),gtk.CellRendererText())						##create a cell renderer
			analyse_treeview.append_column(getattr(self,"analyse_tvcolumn"+str(col)))				##append the column to TreeView
			getattr(self,"analyse_cell"+str(col)).set_property('cell-background', 'white')				##cell background color
			getattr(self,"analyse_tvcolumn"+str(col)).pack_start(getattr(self,"analyse_cell"+str(col)), True)	##add the cells to the columns
        		# set the cell attributes to the appropriate liststore column
        		# GTK+ 2.0 doesn't support the "stock_id" property
        		getattr(self,"analyse_tvcolumn"+str(col)).set_attributes(getattr(self,"analyse_cell"+str(col)), text=col)

		analyse_treeview.set_model(getattr(self,"analyse_liststore"))
		for cpu in self.data:
			getattr(self,"analyse_liststore").append(["CPU "+str(cpu), "n/a", "n/a", "n/a", "n/a"])			##insert empty data 


	def poll_msr(self):
	###get current VIDs from MSR
		getattr(self,"analyse_liststore").clear()									##clear liststore
		for cpu in self.data:
			if self.msrinfo.cpu_have_msr(cpu):
				msrdata=self.msrinfo.read_msr(cpu)
				if self.data[cpu]['voltages']['formula']['available']:
					cVcc = self.voltages.string_voltage_from_vid(self.data[cpu]['voltages']['formula']['name'],msrdata['curV'])+"V"
					tVcc = self.voltages.string_voltage_from_vid(self.data[cpu]['voltages']['formula']['name'],msrdata['tgtV'])+"V"
				else:
					cVcc = "n/a"
					tVcc = "n/a"
				getattr(self,"analyse_liststore").append(["CPU "+str(cpu), str(msrdata['tgtV']), tVcc, str(msrdata['curV']), cVcc])	
			else:
				getattr(self,"analyse_liststore").append(["CPU "+str(cpu), "n/a", "n/a", "n/a", "n/a"])			##insert empty data


#####event handlers#########
	def display_help_popup(self, *argv):
	##open help popup
		phctoolhelp.popup(self.wTree.get_widget("notebook_base").get_current_page())

	def on_vid_spinbutton_change(self, widget, cpu, fid):
	##Throttling sliders have been changed
		if self.data[cpu]['voltages']['formula']['available']:
			nVcc = self.voltages.string_voltage_from_vid(self.data[cpu]['voltages']['formula']['name'],widget.get_value())
			dVcc = self.voltages.string_voltagediff_from_vids(self.data[cpu]['voltages']['formula']['name'], widget.get_value(), self.data[cpu]['phcdefaultvalues'][fid])
		else:
			nVcc = "n/a"
			dVcc = "n/a"
		getattr(self, 'voltage_volttext'+str(cpu)+"_"+str(fid)).set_text(nVcc)
		getattr(self, 'voltage_difftext'+str(cpu)+"_"+str(fid)).set_text(dVcc)

	def on_button_save_clicked(self,widget):
	##save values
        	tmpdata={}
        	for cpu in self.data:
			vidstring = ""
			if not self.data[cpu]['phc']:
				break
            		iter=0
            		for vid in self.data[cpu]["phcvalues"]:
				tmpval = int(getattr(self,'spinbtn'+str(cpu)+str(iter)).get_value()) 	##make integer from float to remove dotted values
				vidstring +=" "+str(tmpval)						##join seperate values to a string...
				self.data[cpu]["phcvalues"][iter] =str(tmpval)				##...and set the value into the data dictionary
               		 	iter += 1
            		tmpdata[cpu]=vidstring.strip()
        	self.cpuinfo.set_phcdata(tmpdata)							##set new vids to the CPUs
		self.phcdata.StoreValues()								##save new values to file


	def on_button_msrrefresh(self,widget):
	##refresh MSR Infos
		self.poll_msr()


	def on_button_restore_clicked(self,widget):
	##restore default VIDs
        	for cpu in self.data:
            		iter=0
            		if self.data[cpu]["phc"] == 1:
                		for vid in self.data[cpu]["phcdefaultvalues"]:
                    			getattr(self, 'spinbtn'+str(cpu)+str(iter)).set_value(int(vid))
                    			iter += 1


	def On_Change_Throttle_Scale(self,widget, cpunr):
	##Throttling sliders have been changed
		value=int(widget.get_value())  		##make interger from float ( 1.0 -> 1 )
		percent=self.throttling.data[cpunr]['states']["T"+str(value)]+"%"
		getattr(self, 'label_TState'+str(cpunr)).set_text(percent)
		self.throttling.set_throttledata(cpunr,value);
		self.phcdata.StoreValues()
		self.RefreshThrottleControls()


	def clicked_restoreopts(self,widget):		
	##get the new options and store them
		opts=""
		if self.wTree.get_widget("checkbutton_reloadvids").get_active():
			opts = opts +"V"
		if self.wTree.get_widget("checkbutton_reloadthrottles").get_active():
			opts = opts +"T"
		self.phcdata.storeopts = opts
		self.phcdata.StoreValues();		##save options and setted values


	def quit(self,widget):
	##quit program
		gtk.mainquit
		sys.exit(0)



class nogui:
	def __init__(self):
		self.phcdata=generic.phc(self)	##functions for PHC
		self.cpuinfo=cpuinfo.cpuinfo()	##functions to gather CPU informations
		self.throttling=throttling.throttlecontrol(self.cpuinfo.data)
		self.phcdata.RestoreValues()	##restore valus that has been set last time

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "background":
        ##just set the values - don't show gui
	ng = nogui()
	sys.exit(0)
    else:
	app=appgui()
	gtk.main()


