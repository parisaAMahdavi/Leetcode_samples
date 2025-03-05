from LinkedList import LinkedList

# This function only remove consecutive duplicates
# For example: 1 -> 1 -> 2 -> 3 -> 3 -> 3 -> 1
# The output will be: 1 -> 2 -> 3 -> 1
# def remove_duplicates(l1):
#     if l1.head is None:
#         return 
#     curr_node = l1.head
#     while curr_node and curr_node.next:
#         if curr_node.val == curr_node.next.val:
#             curr_node.next = curr_node.next.next
#         else:curr_node = curr_node.next
#     return l1


# This function remove all duplicates
# For example: 1 -> 1 -> 2 -> 3 -> 3 -> 3 -> 1
# The output will be: 1 -> 2 -> 3
def remove_duplicates(l1):
    if l1.head is None:
        return
    curr_node = l1.head
    prev_node = None
    while curr_node:
        runner = curr_node
        while runner.next:
            if runner.next.val == curr_node.val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        prev_node = curr_node
        curr_node = curr_node.next
    l1.tail = prev_node
    return l1