from linked_list import LinkedList

#Stack inherits from LinkedList class
class Stack(object):

    def __init__(self, iterable=None):
        if iterable != None:
            self._linkedList = LinkedList(iterable)
        else:
            self._linkedList = LinkedList()

    def push(self, value):
        self._linkedList.insert(value)

    def pop(self):
        try: 
            return self._linkedList.pop()
        except AttributeError:
            print "Error: Stack is empty. Nothing to pop."
            raise