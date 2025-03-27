class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

BT = TreeNode("Drinks")
leftchild = TreeNode("Hot")
rightchild = TreeNode("Cold")
BT.leftchild = leftchild
BT.rightchild = rightchild

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

postOrderTraversal(BT)

