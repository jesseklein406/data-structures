class Node(object):

    def __init__(self, value):
        self.value = value
        self.next_node = None


class LinkedList(object):
    size = 0
    head = None

    def insert(self, val):
        new_node = Node(val)
        new_node.next_node = self.head
        self.head = new_node
        print "head is now", self.head.value

    def display(self):
        pass
        #return self.displayList
    
    def pop(self):
        val = self.head.value
        self.head = self.head.next_node
        return val

    #def size():

    #def search(val):



l1 = LinkedList()
l1.insert(5)
print
print
l1.insert(7)
l1.insert(9)
l1.insert(10)
l1.insert(33)

print
print

print l1.pop()
print l1.pop()
