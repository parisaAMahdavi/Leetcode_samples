import sys
sys.path.append("/Users/parisa/coding/Leetcode_samples/LinkedLists")
from LinkedList import Queue


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

BT = TreeNode("Drinks")
leftchild = TreeNode("Hot")
rightchild = TreeNode("Cold")
leftchild.leftchild = TreeNode("tea")
leftchild.rightchild = TreeNode("coffee")
# rightchild.leftchild = TreeNode("cola")
# rightchild.rightchild = TreeNode("juice")
BT.leftchild = leftchild
BT.rightchild = rightchild
BT.leftchild.leftchild = leftchild.leftchild
BT.leftchild.rightchild = leftchild.rightchild
# BT.rightchild.leftchild = rightchild.leftchild
# BT.rightchild.rightchild = rightchild.rightchild


def preOrderTraversal(rootNode): #time complexity O(n)
    if rootNode is None:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftchild)
    preOrderTraversal(rootNode.rightchild)

def inOrderTraversal(rootNode):
    if rootNode is None:
        return None
    inOrderTraversal(rootNode.leftchild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightchild)   

def postOrderTraversal(rootNode):
    if rootNode is None:
        return None
    postOrderTraversal(rootNode.leftchild)
    postOrderTraversal(rootNode.rightchild)
    print(rootNode.data)

def levelOrderTraversal(rootNode):
    """
    For level order traversal, time and space complexity is O(n) because we are using a queue to store the nodes
    and we are visiting each node once.
    """
    if rootNode is None:
        return None
    queue = Queue()
    queue.enqueue(rootNode)

    while not(queue.isEmpty()):
        root = queue.dequeue()
        print(root.val.data)
        if root.val.leftchild is not None:
            queue.enqueue(root.val.leftchild)
        if root.val.rightchild is not None:
            queue.enqueue(root.val.rightchild)
def searchBT(rootNode, value):
    """
    For searching a value in the binary tree, we will use the level order traversal as it is based on queue"
    """
    if rootNode is None:
        return None
    queue = Queue()
    queue.enqueue(rootNode)
    while not(queue.isEmpty()):
        root = queue.dequeue()
        if root.val.data == value:
            return root.val.data
        if root.val.leftchild is not None:
            queue.enqueue(root.val.leftchild)
        if root.val.rightchild is not None:
            queue.enqueue(root.val.rightchild)
    return "Not Found"
    
def insertNodeBT(rootNode, value):
    if rootNode is None:
        rootNode = value
    else:
        queue = Queue()
        queue.enqueue(rootNode)
        while not(queue.isEmpty()):
            root = queue.dequeue()
            if root.val.leftchild is not None:
                queue.enqueue(root.val.leftchild)
            else:
                root.val.leftchild = value
                return "inserted new node"
            if root.val.rightchild is not None:
                queue.enqueue(root.val.rightchild)
            else:
                root.val.rightchild = value
                return "inserted new node"
def findDeepestNode(rootNode):
    if rootNode is None:
        return None
    queue = Queue()
    queue.enqueue(rootNode)
    while not(queue.isEmpty()):
        root = queue.dequeue()
        if root.val.leftchild is not None:
            queue.enqueue(root.val.leftchild)
        if root.val.rightchild is not None:
            queue.enqueue(root.val.rightchild)
    return root.val
def deleteDeepestNode(rootNode, dNode):
    if rootNode is None:
        return 
    queue = Queue()
    queue.enqueue(rootNode)
    while not(queue.isEmpty()):
        root = queue.dequeue()
        if root.val is dNode:
            root.val = None
            return "deleted the deepest node"
        if root.val.rightchild:
            if root.val.rightchild is dNode:
                root.val.rightchild = None
                return "deleted the deepest node"
            else:
                queue.enqueue(root.val.rightchild)
        if root.val.leftchild:
            if root.val.leftchild is dNode:
                root.val.leftchild = None
                return "deleted the deepest node"
            else:
                queue.enqueue(root.val.leftchild)
def deleteNodeBT(rootNode, value):
    if rootNode is None:
        return None
    queue = Queue()
    queue.enqueue(rootNode)
    while not(queue.isEmpty()):
        root = queue.dequeue()
        if root.val.data == value:
            dNode = findDeepestNode(rootNode)
            root.val.data = dNode.data
            deleteDeepestNode(rootNode, dNode)
            return "deleted the node"
        else:
            if root.val.leftchild is not None:          
                queue.enqueue(root.val.leftchild)
            if root.val.rightchild is not None:
                queue.enqueue(root.val.rightchild)
    return 'Not Found'

