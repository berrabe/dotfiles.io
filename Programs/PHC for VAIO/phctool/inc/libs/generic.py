#generic.py
#This file contains generic functions for PHCtool


import sys
import os, re
import string

class phc:
    def __init__(self, parent):
        self.cpuinfos={};
        self.storeopts={} 				##value store options
	self.parent=parent				##parent object
	self.storefile=os.environ.get("HOME")+"/.phcstore.phc"

    def StoreValues(self): 				##store values into a textfile to reload them
        store = file(self.storefile, "w")
	data= self.parent.cpuinfo.data
	if len(data)>0:
		store.write("R="+str(self.storeopts)+"\n")
        	for cpu in data:
			if data[cpu].has_key('phcvalues'):
	            		store.write(str(cpu)+": V="+" ".join(data[cpu]["phcvalues"])+" T="+str(self.parent.throttling.data[cpu]["active_state"])+"\n")
        	store.close()
    	else:
		print "ERROR writing store file: data array empty"


    def RestoreValues(self): 				##read and apply values from storing file
        if os.path.exists(self.storefile):
            store = file(self.storefile,"r");
            vids = {}
            throttles = {}
	    opts=""
	    for line in store:
                if len(line) > 1:  			##is there any data, not just an empty line?
                    line = line.strip() 		##remove spaces
                    if line[0] != "#":  		##not a comment ?
                        cpu = line[:line.find(":")]
			if line.find("R=")>=0:
				opts= string.strip(line[line.find("R=")+2:])
			
			if line.find("V=")>1:
                        	vids[cpu]= string.strip(line[line.find("V=")+2:line.find("T=")-1])

			if line.find("T=")>1:
				throttles[cpu]= string.strip(line[line.find("T=")+2:])

	    self.storeopts=opts
            store.close();

	    if "V" in opts:				##restore VIDs enabled?
		self.parent.cpuinfo.set_phcdata(vids)
	    if "T" in opts:				##restore VIDs enabled?
		self.parent.throttling.set_throttledata_array(throttles)
	    return 0
	else:
		print "File ",self.storefile," not found. Not a problem but there are no values to restore."
		print "But because I like you, I'll create a new one."
		self.StoreValues()
	    	self.storeopts=""
	    	return 1 				##store file does not exist ...
