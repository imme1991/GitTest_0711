#coding:utf-8
from python_class.classPerson import *
p1 = Person("zhang", "186", "beijing")
p1.printInfo()
p2 = Person("li", "188", "xian")
p2.printInfo()

p1 = p1 + p2
p1.printInfo()
