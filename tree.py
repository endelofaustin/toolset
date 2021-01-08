#!/usr/bin/python

class BinaryTree():

    def __init__(self, root):

        self.root = root
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None
            self.leftChild = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.leftChild = self.leftChild
            self.leftChild = tree

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.rightChild = self.rightChild
            self.rightChild = tree

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.root = obj

    def getRootVal(self):
        return self.root

