#coding:utf-8
from classPerson import *
class EducationOfPerson(Person):
	#def __init__()
	schoolname = []
	def addSchool(self, schoolname):
		self.schoolname.append(schoolname)

	def printInfo(self):
		print self.name, "\n", self.phone, "\n", self.address, "\n", self.schoolname

