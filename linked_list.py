#class LinkedListNode(object):
#
#    def __init__(self, value):
#
#        self.value = value
#        self.nextnode = None
#        self.head = None
#
#    def add_to_linked_list(self, value):
#
#        n1 = LinkedListNode(None)
#        n2 = LinkedListNode(None)
#        n3 = LinkedListNode(None)
#        n1.value = n.head
#        n1.nextnode = n2
#        n2.nextnode = n3
#        
#

class Node:

    def __init__(self):
        self.head = Node()

class linked_list:

    def __init__(self, value):
        self.head = Node()

    def append(self, value):
        new_node = Node(value)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

    def length(self):
        current = self.head
        total = 0
        while current.next != None:
            total += 1 
            current = current.next
        return total

    def display(self,):
        elements = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            elements.append(current_node.value)
        print elements



