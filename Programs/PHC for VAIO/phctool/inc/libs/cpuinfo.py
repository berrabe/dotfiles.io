#cpuinfo.py
#This is a function library to get 
#informations about CPUs and its PHC data
#Modified by Fabio Veronese fveronese85*at*gmail.com 6 Mar 2011


import os, string

class cpuinfo:
	def __init__(self):
		self.cpucount=0
		self.data={}
		self._get_acpi_cpus()		##get ACPI-supported CPUs
		self._get_cpuinfos()		##get Infos from /proc/cpuinfo for every ACPI-CPU we found


	def _get_acpi_cpus(self):
		# We need to ignore /proc/acpi/processor as it's becoming deprecated
		# A good solution might be a look in online cpus, but it doesn't mean they are surely ACPI-supported
		if os.path.exists('/sys/devices/system/cpu/online'):
			file = open('/sys/devices/system/cpu/online', 'r');
			for line in file:
				content = line.split("-");
				if (len(content)==1):
					cpurange=int(content[0].strip())+1
				else:
					cpurange=int(content[1].strip())+1
				for intcpunr in range(cpurange):
					cpunr=str(intcpunr)
					self.data[cpunr]={}
					self.data[cpunr]['acpi']={}
					self.data[cpunr]['acpi']['exist']=True
		# This sounds useful just for throttling, which is managed better by other stuff... I'll keep just for compatibility
					if os.path.exists('/proc/acpi/processor/CPU'+cpunr):
						##remember ACPI Pathname
						self.data[cpunr]['acpi']['acpiname']='/proc/acpi/processor/CPU'+cpunr
					elif os.path.exists('/sys/devices/system/cpu/cpu'+cpunr+'/thermal_throttle'):
						##here some throttling infos for 2.6.38 and maybe laters
						self.data[cpunr]['acpi']['acpiname']='/sys/devices/system/cpu/cpu'+cpunr+'/thermal_throttle'
					else:
						self.data[cpunr]['acpi']['acpiname']='/sys/devices/system/cpu/cpu'+cpunr+'/topology'
						self.data[cpunr]['acpi']['exist']=False
		# For some reason we have to fallback on the old function...
		else:
			directory="/proc/acpi/processor/"
			for f in os.listdir(directory):				##iterate the directory
				pathname = os.path.join(directory, f)		##
        			if os.path.isdir(pathname):			##is the object we found really a (sub-)directory?
					##We open the info-file to get the ID to this CPU,
					##i don't know if this really could happen but the ID may differ from 
					##from the Path iterator (maybe one CPU is supported and another isn't)
					if os.path.exists(pathname+'/info'):
						file = open(pathname+'/info', 'r');
						for line in file:
			   				if string.find(line,":"):
			     					content = line.split(":");
			    	 				if len(content)>1:
									info_ident=content[0].strip();
									info_value=content[1].strip();
									if info_ident == "processor id":
										cpunr=info_value
										self.data[cpunr]={}
										self.data[cpunr]['acpi']={}
										self.data[cpunr]['acpi']['exist']=True
										self.data[cpunr]['acpi']['acpiname']=f	##remember ACPI Pathname
					else:
						self.data[cpunr]['acpi']['exist']=False
		

	def _get_cpuinfos(self):
	##get infos about the CPUs from /proc/cpuinfos, etc
		file = open("/proc/cpuinfo", "r");
		tmp={}
		
		for line in file:
		   	if string.find(line,":"):
		     		content = line.split(":");
		    	 	if len(content)>1:
					info_ident=content[0].strip();
					info_value=content[1].strip();
					if info_ident == "processor":
						cpunr=info_value;
						tmp[cpunr]={}
						tmp[cpunr]["modelid"]={}

					elif info_ident == "model name":
						tmp[cpunr]["model"] = info_value
					elif info_ident == "vendor_id":
						tmp[cpunr]["modelid"]["vendor_id"]=info_value
					elif info_ident == "cpu family":
						tmp[cpunr]["modelid"]["family"]=info_value
					elif info_ident == "model":
						tmp[cpunr]["modelid"]["model"]=info_value
					elif info_ident == "stepping":
						tmp[cpunr]["modelid"]["stepping"]=info_value
		file.close()


		for cpu in tmp:
			if self.data.has_key(cpu):		##is this CPU affinated with ACPI?
				self.data[cpu].update(tmp[cpu])	##store datas
				self._get_phc(cpu)		##get PHC infos
				self._get_freqsteps(cpu)	##get frequency steps



	def _get_phc(self, cpunr):
	##check if PHC is available and if, store default and current Values
		if os.path.exists('/sys/devices/system/cpu/cpu'+cpunr+'/cpufreq/phc_vids'):
			self.data[cpunr]["phc"]=True
			self.data[cpunr]["phcvalues"]=self._get_PHCData(cpunr)
			self.data[cpunr]["phcdefaultvalues"]=self._get_PHCDefaultData(cpunr)
			self.data[cpunr]["phcversion"]=self._get_PHCVersion(cpunr)
		else:
			self.data[cpunr]["phc"]=False


    	def _get_PHCVersion(self, cpunr): 		##read PHC-Version from the phc interface
		data = "failed"
        	phcif = file("/sys/devices/system/cpu/cpu"+cpunr+"/cpufreq/phc_version", "r");
        	for line in phcif:
            		if len(line) > 1: 	##is there any data, not just an empty line?
                		data=line.strip();
        	phcif.close()
        	return data   

    	def _get_PHCData(self, cpunr): 		##read VIDs from the phc interface
		data = {}
        	phcif = file("/sys/devices/system/cpu/cpu"+cpunr+"/cpufreq/phc_vids", "r");
        	for line in phcif:
            		if len(line) > 1: 	##is there any data, not just an empty line?
                		data=line.split();
        	phcif.close()
        	return data   

    
    	def _get_PHCDefaultData(self, cpunr):
	##get default VIDs 
    		data = {}
       		phcif = file("/sys/devices/system/cpu/cpu"+cpunr+"/cpufreq/phc_default_vids", "r");
        	for line in phcif:
            		if len(line) > 1:  	##is there any data, not just an empty line?
                		data=line.split();
        	phcif.close()
        	return data

	def _get_freqsteps(self, cpunr):
	##get available frequency-steps for this cpu from
	##/sys/devices/system/cpu/cpu{{0}}/cpufreq/scaling_available_frequencies
		if os.path.exists('/sys/devices/system/cpu/cpu'+cpunr+'/cpufreq/scaling_available_frequencies'):
			ffile= file('/sys/devices/system/cpu/cpu'+cpunr+'/cpufreq/scaling_available_frequencies','r')
			freqs = ffile.readline().strip().split(' ')	##force sorting the freqs descending. 
			freqs = map(int, freqs)					##change data type to int to sort it by number (dirty workaround)
			freqs.sort(reverse=True)			##speedstep-centrino displays them different to acpi-cpufreq
			freqs = map(str, freqs)					##change data type back to str
			self.data[cpunr]['frequencies']= freqs
			self.data[cpunr]['stepping']=True
			ffile.close()
		else:
			self.data[cpunr]['stepping']=False

    	def set_phcdata(self, phcdata):
	##write uservalues to phc interface
	##phcdata looks like this:  {'1': '39 33 26 19', '0': '39 33 26 19'}
        	for cpunr in phcdata:
	  		if os.path.exists("/sys/devices/system/cpu/cpu"+cpunr+"/cpufreq/phc_vids"):
			    try:
            			phcif = file("/sys/devices/system/cpu/cpu"+cpunr+"/cpufreq/phc_vids", "w")
            			phcif.write(str(phcdata[cpunr]))
            			phcif.close()
				self._get_phc(cpunr)		##refresh VIDs in Array
			    except:
				print "ERROR while writing VIDs to interface."

	def cpu_have_phc(self, cpu):
	##return if PHC is available to the CPU or not
		return self.data[cpu]['phc']

	def phc_version(self, cpu):
	##return if PHC is available to the CPU or not
		return self.data[cpu]['phcversion'].strip()


