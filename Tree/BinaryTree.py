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
rightchild.leftchild = TreeNode("cola")
rightchild.rightchild = TreeNode("juice")
BT.leftchild = leftchild
BT.rightchild = rightchild
BT.leftchild.leftchild = leftchild.leftchild
BT.leftchild.rightchild = leftchild.rightchild
BT.rightchild.leftchild = rightchild.leftchild
BT.rightchild.rightchild = rightchild.rightchild


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


levelOrderTraversal(BT)

