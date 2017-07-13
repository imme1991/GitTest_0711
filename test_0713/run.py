#coding:utf-8
#main
from parser_class import *
from rparser_class import *
from node_class import *

#创建node节点
a = Node("a", "0", "1")
b = Node("b", "1", "11")
c = Node("c", "1", "12")
d = Node("d", "11", "112")
j = Node("j", "0", "2")
h = Node("h", "2", "21")

nodeLlist = [a, b, c, j, d, h]

#进行parser
treeList = []
p = Parser(nodeLlist)
p.parser("0", treeList)
print(treeList)

#进行rparser
q = RParser(treeList)
q.rparser("0", treeList)
q.printNode()