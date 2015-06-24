class Node(object):

    def __init__(self, value):
        self.value = value
        self.next_node = None


class LinkedList(object):
    displayList = []
    size = 0
    head = None

    def insert(self, val):
        self.displayList.insert(0, val)

        new_node = Node(val)
        new_node.next_node = self.head
        self.head = new_node
        print "head is now", self.head.value
        print "displayList: ", self.displayList

    def display(self):
        return self.displayList
    
    def pop(self):
        val = self.head.value
        self.displayList.pop(0)
        self.head = self.head.next_node
        print "displayList: ", self.displayList

        return val

    #def size():

    #def search(val):



l1 = LinkedList()
l1.insert(5)
print
print "display():", l1.display()
print
l1.insert(7)
l1.insert(9)
l1.insert(10)
l1.insert(33)

print
print "display():", l1.display()
print

print l1.pop()
print l1.pop()
