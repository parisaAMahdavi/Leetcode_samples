from LinkedList import LinkedList
import random

# This method will partition the linked list around a value x 
# such that all nodes less than x come before all nodes greater than or equal to x
def partition(l1, x):

    curr_node = l1.head
    l1.tail = l1.head  # set the tail to the head to prevent cycle when the tail is updated

    while curr_node:
        next_node = curr_node.next
        curr_node.next = None
        if curr_node.val < x:
            curr_node.next = l1.head
            l1.head = curr_node
        else:
            l1.tail.next = curr_node
            l1.tail = curr_node
        
        curr_node = next_node
    if l1.tail.next is not None:
        l1.tail.next = None
    return l1

random.seed(10)
linkded_list = LinkedList()
linkded_list.generate(10, 0, 99)
print(linkded_list)


# partition(linkded_list, 30)
# print(linkded_list)
# print(linkded_list.head.val)
# print(linkded_list.tail.val)    