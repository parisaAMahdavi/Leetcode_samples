
import random
class Node:
    def __init__(self,value=None):
        self.val = value
        self.next = None
        self.prev = None
    
    def __str__(self):
        return str(self.val)
    
class LinkedList:
    def __init__(self, values = None):
        self.head = None
        self.tail = None
    def __iter__(self):
        curr_node = self.head
        while curr_node:
            yield curr_node
            curr_node = curr_node.next
    def __str__(self):
        res = " "
        curr_node = self.head
        while curr_node:
            res += str(curr_node.val) 
            curr_node = curr_node.next
            if curr_node:
                res += " -> "
        return res
    def __len__(self):
        res = 0
        curr_node = self.head
        while curr_node:
            res += 1
            curr_node = curr_node.next
        return res
    def add(self, value):
        if self.head == None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail
    def generate(self, n, min_val, max_val):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(random.randint(min_val, max_val))
        return self


# linked_list = LinkedList()
# linked_list.generate(10, 0, 99)
# print(linked_list)
# print(len(linked_list))



