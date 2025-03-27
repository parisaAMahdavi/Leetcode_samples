
from LinkedList import LinkedList

def sum_linkedlist(l1,l2):
    '''
    # FIRST APPROACH - CONVERT TO INTEGER, ADD AND CONVERT BACK TO LINKED LIST, NOT OPTIMIZED
    # curr1 = l1.head
    # curr2 = l2.head
    # l3 = LinkedList()
    # n = 0
    # m = 0
    # dig1 = 0
    # dig2 = 0
    
    # while curr1:
    #     dig1 += curr1.val * 10**(n)
    #     n+=1
    #     curr1 = curr1.next
    # while curr2:
    #     dig2 += curr2.val * 10**(m)
    #     m+=1
    #     curr2 = curr2.next
    # res = int(dig1) + int(dig2)
    # print(res)
    # while res!=0 :
    #     l3.add(res%10)
    #     res = res//10

    #SECOND APPROACH - ADD DIGITS AND CARRY, IT CAN BE USED ONLY IF BOTH LINKED LISTS HAVE SAME LENGTH
    # curr1 = l1.head
    # curr2 = l2.head
    # l3 = LinkedList()
    # carry = 0
    # while curr1 or curr2:
    #     sum = curr1.val +curr2.val + carry
    #     carry = sum//10
    #     l3.add(sum%10)

    #     curr1 = curr1.next
    #     curr2 = curr2.next
    # return l3'
    '''
    #THIRD APPROACH - ADD DIGITS AND CARRY, IT CAN BE USED ONLY IF BOTH LINKED LISTS HAVE SAME LENGTH
    curr1= l1.head
    curr2= l2.head
    l3 = LinkedList()
    carry = 0
    while curr1 or curr2:
        sum = carry
        if curr1:
            sum += curr1.val
            curr1 = curr1.next
        if curr2:
            sum += curr2.val
            curr2 = curr2.next
        l3.add(sum%10)
        carry = sum//10
    return l3
