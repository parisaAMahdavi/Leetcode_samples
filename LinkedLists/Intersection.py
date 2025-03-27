from LinkedList import LinkedList, Node

def define_intersection_node(l1,l2):
    '''
    Given two singly linked lists, determine the node where the two lists merged.
    The time comlexity of this algorithm is O(A+B) where A and B are the lengths of the two linked lists.
    '''

    if l1.tail != l2.tail:
        return False

    len1 = len(l1)
    len2 = len(l2)

    shortlist  = l1 if len1<len2 else l2
    longlist = l1 if len1>len2 else l2
    diff = len(longlist) - len(shortlist)

    longer_head = longlist.head
    shorter_head = shortlist.head

    for i in range(diff):
        longer_head = longer_head.next

    while longer_head != shorter_head:
            longer_head = longer_head.next
            shorter_head = shorter_head.next
    return longer_head

def addSameNode(l1,l2,value):
     
     node = Node(value)
     l1.tail.next = node
     l2.tail.next = node
     l1.tail = node
     l2.tail = node
     
# l1 = LinkedList()
# l2 = LinkedList()

# l1.generate(3, 0, 20)
# l2.generate(4, 0, 20)
# addSameNode(l1,l2,10)
# addSameNode(l1,l2,11)
# addSameNode(l1,l2,12)

# print(l1)
# print(l2)


        
# intersection_node = define_intersection_node(l1,l2)
# print(intersection_node)