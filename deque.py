#!/usr/bin/python

class Deque():
    
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRead(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


