#voltages.py
#this library provides functions to calculate Voltages from VID if CPU model is known
#



class voltage:
	def __init__(self, cpudata):
		self.cpudata = cpudata
		for cpu in self.cpudata:
				##extend array
			self.cpudata[cpu]['voltages']={}
			self.cpudata[cpu]['voltages']['formula']={}
			self._get_formula_name(cpu)


########################################################################################

	def _get_formula_name(self, cpu):
	#Get the name of the formular to use
	#by an array of CPU Identification Data
	#the array have to contain at least those data:
	#['vendor_id':'GenuineIntel'; 'family':'6'; 'model':'14']
	
		formula = 0
		if self.cpudata[cpu]['modelid']['vendor_id'] == "GenuineIntel":
		##we have an Intel CPU
			if self.cpudata[cpu]['modelid']['family'] == "6":
				if self.cpudata[cpu]['modelid']['model'] == "13":
				##Pentium M
					formula = "pentium_m";
		
				elif self.cpudata[cpu]['modelid']['model'] == "14":
				##Core Duo
					formula = "coreduo";
	
				elif self.cpudata[cpu]['modelid']['model'] == "15":
				##Core Duo
					formula = "coreduo";

				elif self.cpudata[cpu]['modelid']['model'] == "23":
				##Core Duo Penryn
					formula = "coreduo";

		#elif cpuid['vendor_id'] == "AuthenticAMD":
		##we have an AMD CPU

		if formula == 0:
			self.cpudata[cpu]['voltages']['formula']['available'] = False;
		else:	
			self.cpudata[cpu]['voltages']['formula']['available'] = True;
			self.cpudata[cpu]['voltages']['formula']['name'] = formula;



	def voltage_from_vid(self, formula, vid):
	#this calculates the Voltages from VIDs
	#The formulas may fit different cpu series
		VID = int(vid)
		voltage = 0
		if formula == "pentium_m":
		##Pentium M (centrino)
			voltage = (700.0 + (VID * 16))/1000

		if formula == "coreduo":
		##Core and Core2 CPUs
			voltage = (712.5 + (VID * 12.5))/1000

		if formula == "amd_64":
		##Athlon64, Turion, Opteron.
		##Found in the internet - not yet verified 
			voltage = (1550.0-(VID * 25))/1000

		return voltage


	def voltagediff_from_vids(self, formula, vid1, vid2):
		vid1=self.voltage_from_vid(formula, vid1)
		vid2=self.voltage_from_vid(formula, vid2)
		voltage = vid2 - vid1
		return voltage

	def string_voltagediff_from_vids(self, *args):
	##return a formatted string from voltages difference
		voltage=self.voltagediff_from_vids(*args)	
		return(self.fmtstring_from_voltage(voltage))

	def string_voltage_from_vid(self, *args):
	##return a formatted string from voltage
		voltage = self.voltage_from_vid(*args)
		return(self.fmtstring_from_voltage(voltage))

	def fmtstring_from_voltage(self, voltage):
	##format a voltage to a string with AT LEAST 4 digits
		tmp = str(voltage)
		if len(tmp[tmp.find(".")+1:]) < 4:
			return "%1.4f" % voltage
		else:
			return tmp





