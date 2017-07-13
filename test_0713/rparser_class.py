#coding:utf-8
#rparser: get nodes from trees
from node_class import *
class RParser:
	nodeList = []
	def __init__(self, treeList):
		self.treeList = treeList

	def printTree(self):
			print(self.treeList)

	def rparser(self, rootId, tree):
		for i in tree:
			node = Node(i["name"], rootId, i["id"])
			self.nodeList.append(node)
			self.rparser(i["id"], i["member"])
	
	def printNode(self):
		for i in self.nodeList:
			print(i.name, i.parentId, i.Id)


