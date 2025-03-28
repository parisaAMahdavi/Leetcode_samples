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
    


print(searchBT(BT, "orange"))

