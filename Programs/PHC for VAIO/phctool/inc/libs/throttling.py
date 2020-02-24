#throttling.py
#Throttling function library for PHCtool


import os, string

class throttlecontrol:
	def __init__(self,cpudata):				##need an array of available CPUs
		self.cpus=cpudata
		self.data={}					##create dictionary for storing our values
		for cpu in self.cpus:
			self.data[cpu]={}
			self.data[cpu]['states']={}
			self.data[cpu]['active_state']=""
			self.data[cpu]['state_count']=""
		self._cpus_have_interface()			##check which CPU has a trottling interface
		self._throttling_values()			##get Throttling Values fpr each CPU that have an interface


	def _cpus_have_interface(self):
	##check if the given CPU has a throttling interface
		for cpu in self.cpus:
			if os.path.exists('/proc/acpi/processor/'+self.cpus[cpu]['acpi']['acpiname']+'/throttling') & os.path.exists('/proc/acpi/processor/'+self.cpus[cpu]['acpi']['acpiname']+'/limit'):
				tfile = open('/proc/acpi/processor/'+self.cpus[cpu]['acpi']['acpiname']+'/throttling', 'r');
				for line in tfile:
					if string.find(line,"not supported") >= 0:
						self.data[cpu]['exist'] = False
					else:
						self.data[cpu]['exist'] = True
				tfile.close()
			else:
				self.data[cpu]['exist'] = False
			

	def _throttling_values(self):
	#Get Available Throttling States and the current activated State
		for cpu in self.cpus:
			if self.data[cpu]['exist']:
			    tfile = open('/proc/acpi/processor/'+self.cpus[cpu]['acpi']['acpiname']+'/throttling', 'r');
			    for line in tfile:
				if string.find(line,":"):					##is there a seperator?
			     		content = line.split(":");				##divide it
			     		if len(content) > 1:					##is there a attribute-value pair?
						if content[0] == "state count":			##count of available states
							self.data[cpu]['state_count'] = int(content[1]);
						elif content[0] == "active state":		##the current active State
							state=content[1].strip();
							self.data[cpu]['active_state'] = int(state[1:])
						elif content[0].strip()[0] in ["T","*"]:	##Get the states and its throttling percentage values
							state=content[0].strip().strip('*')
							percentage=content[1].strip().strip('%')
							self.data[cpu]["states"][str(state)] = str(percentage)
			    tfile.close()


    	def _write_state(self, cpu, value):
	##write a Throttling State to the acpi interface
		if self.data[cpu]['exist']:
			try:
				lfile=file('/proc/acpi/processor/'+self.cpus[cpu]['acpi']['acpiname']+'/limit', "w")
				lfile.write("0:"+str(value)+"\n")
				lfile.close()
			except:
				print "Error while writing throttling states. ACPI throttling interface exist but something is strange here."

    	def set_throttledata(self, cpu, value):
	##set a new throttling value to the given CPU
		if self.data.has_key(cpu):					##is this CPU number available (should be, this is for errors only)
			if int(value) >= 0 and int(value)< self.data[cpu]["state_count"]:
				self._write_state(cpu, value)			##write the new value to the interface		
				self._throttling_values()			##reload data from interface (to check if the new value is assigned)


    	def set_throttledata_array(self, array):
	##set a new throttling value to the given CPU
		for cpu in array:
			self.set_throttledata(cpu, array[cpu])
		
