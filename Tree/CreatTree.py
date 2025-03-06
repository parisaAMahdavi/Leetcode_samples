class TreeNode:
    def __init__(self, data, children= []):
        self.data = data
        self.children = children
    def __str__(self, level=0):  # level is used to keep track of tree depth
        ret = " " * level + str(self.data) + "\n" # " "*level is used to creat a str of spaces for indentaion
        for child in self.children:
            ret += child.__str__(level + 1) #__str__ is called recursively to print the children of the current node
        return ret
    def addChild(self, TreeNode):
        self.children.append(TreeNode)


# tree = TreeNode("Drinks", [])
# cold = TreeNode("Cold", [])
# hot = TreeNode("Hot", [])
# tree.addChild(cold)     
# tree.addChild(hot)

# tea = TreeNode("tea", [])
# coffee = TreeNode("coffee", [])
# cola = TreeNode("cola", [])
# juice = TreeNode("juice", [])

# cold.addChild(cola)
# cold.addChild(juice)

# hot.addChild(tea)
# hot.addChild(coffee)

# print(tree)