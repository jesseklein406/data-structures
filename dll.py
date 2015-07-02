class Node(object):

    def __init__(self, val):
        self.val = val
        self.next_node = None
        self.prev_node = None


class Dll(object):

    def __init__(self, iterable=None):
        self.sizeOfList = 0
        self.head = None
        self.tail = None

        if iterable is not None:
            for item in iterable:
                self.insert(item)

    def insert(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head.prev_node = new_node
            self.head = new_node

        self.sizeOfList += 1

    def append(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
            self.tail = new_node

        self.sizeOfList += 1

    def pop(self):
        if self.head is None:
            raise IndexError
        elif self.head is self.tail:
            val = self.head.val
            self.head = self.tail = None
        else:
            val = self.head.val
            self.head = self.head.next_node
            self.head.prev_node = None
        self.sizeOfList -= 1
        return val

    def shift(self):
        if self.tail is None:
            raise IndexError
        val = self.tail.val
        if self.tail.prev_node is None:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev_node
            self.tail.next_node = None

        self.sizeOfList -= 1
        return val

    def remove(self, val):

        if self.head is None:
            raise ValueError
        else:
            current = self.head
            while current is not self.tail and current.val != val:
                current = current.next_node

            if current.val == val:
                if current is self.head:
                    self.head = self.head.next_node
                    self.head.prev_node = None
                else:
                    current.prev_node.next_node = current.next_node
                    current.next_node.prev_node = current.prev_node
            else:
                raise ValueError
            self.sizeOfList -= 1
        return current

    def size(self):
        return self.sizeOfList

    def display(self):
        current = self.head
        result = ()
        while current is not None:
            result += (current.val,)
            current = current.next_node
        return result
