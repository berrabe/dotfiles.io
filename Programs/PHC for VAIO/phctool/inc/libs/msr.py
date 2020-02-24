#This is an Interface to the MSR device.
#To use this the kernel module "msr" needs to be loaded.
#It gets the actual VID and FID and the target VID and FID

import os

###some offsets
MSR_IA32_PERF_STATUS=int(0x198)
MSR_IA32_PERF_CTL=int(0x199)


class msr_interface:
	def __init__(self):	
		self.ERR={}
		self.ERR["id"]=0		##error id is 0 (no errors)
		self.ERR["msg"]=""		##error message (something to read for the user)


	def cpu_have_msr(self, cpu):
		if os.path.exists("/dev/cpu/"+str(cpu)+"/msr"):
			return 1
		else:
			return 0


	def read_msr(self, cpu):
		msr_values={}
		if os.path.exists("/dev/cpu/"+str(cpu)+"/msr"):
		   try:
			msrfile = os.open("/dev/cpu/"+str(cpu)+"/msr", os.O_RDONLY);
			os.lseek(msrfile, MSR_IA32_PERF_STATUS, 0);	##jump to where current values lie
			value = os.read(msrfile, 8)			##read 8 bytes
			msr_values['curV']=ord(value[0])		##current voltage Identifer
			##msr_values['curF']=ord(value[1])		##current frequency Identifer
			os.lseek(msrfile, MSR_IA32_PERF_CTL, 0);	##jump to where target values lie
			value = os.read(msrfile, 8)			##read 8 bytes
			msr_values['tgtV']=ord(value[0])		##target voltage Identifer
			##msr_values['tgtF']=ord(value[1])		##target frequency Identifer
			os.close(msrfile)
		   except:
			self.ERR["id"]=2
			self.ERR["msg"]="Cannot read file \"/dev/cpu/"+str(cpu)+"/msr not found.\". Are you root?"
		else:
			self.ERR["id"]=1
			self.ERR["msg"]="File \"/dev/cpu/"+str(cpu)+"/msr not found.\""
		return msr_values


