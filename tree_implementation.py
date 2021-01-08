#!/usr/bin/python

class Tree():
    
    def __init__(self,):
        self.root_node = None

class Node:
    def __init__(self, value):
        self.value = value
        self.child = []
    
    def addChild(self, child):
        self.children.append(child)

root_node = Node(6)
node_17 = Node(17)
root_node.addChild(node_17)

s = Stack()

def traverse_tree():

    while True:
        if s.top.value == 81:
            print('success')
            return False
        else:
            trash = s.pop()
            s.push(trash.children)


