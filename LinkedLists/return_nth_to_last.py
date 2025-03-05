from LinkedList import LinkedList

def nthToLast(l1, n):
    p1 = l1.head
    p2 = l1.head
    for _ in range(n-1):
        p2 = p2.next
        if p2: continue
        else: return None
    while p2.next:
        p2 = p2.next
        p1 = p1.next
    return p1






