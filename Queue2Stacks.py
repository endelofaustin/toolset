#!/usr/bin/python

class Queue2Stacks:

    def __init__(self):
        self.instack = []
        self.outstack = []

    def enque(self, element):
        self.instack.append(element)

    def dequeue(self):
        
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())

        return self.outstack.pop()

