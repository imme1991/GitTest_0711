#coding:utf-8
#parser: build a tree from nodes
from node_class import *
class Parser:
	def __init__(self, allNode):
		self.nodeList = allNode

	def printNodeName(self):
		for i in self.nodeList:
			print(i.name)

	def parser(self, rootId, treeList):
		for i in self.nodeList:
			if i.parentId == rootId:
				nodeDict = {"name":[], "id":[], "member":[]}
				nodeDict["name"] = i.name
				nodeDict["id"] = i.Id
				temp = self.parser(i.Id, nodeDict["member"])
				if temp != None:
					nodeDict["member"].append(temp)
				treeList.append(nodeDict)
		