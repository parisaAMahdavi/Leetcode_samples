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

preOrderTraversal(BT)



