#coding:utf-8
class Person:
	def __init__(self, name, phone, address):
		self.name = name
		self.phone = phone
		self.address = address

	def changeName(self, name):
		self.name = name

	def printInfo(self):
		print self.name, "\n", self.phone, "\n", self.address

	def __add__(self, other):
		self.name += other.name
		self.phone = self.phone + "/" + other.phone
		return self