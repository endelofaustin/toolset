#!/usr/bin/python

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:

    def __init__(self):
        self.top = None

    def push(self, value):
        n = Node(value)
        n.next = self.top
        self.top = n

    def pop(self, value):
        self.top = self.top.next
        print(str(self.top))
        return value

     
    # def __str__(self,):
      #   return Stack

s = Stack()
s.push(5)
s.push(79)
s.push(8414)

s.pop(5)
print(s)

