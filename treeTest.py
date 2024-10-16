class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def root(self,val):
        self.root = Node(val)
        return self.root
    
    def insert(self,root,node):
        if root is None:
            root = node
        if root.data > node.data:
            if root.left is None:
                root.left = node
            else:
                self.insert(root.left,node)
        else:
            if root.right is None:
                root.right = node
            else:
                self.insert(root.right,node)

    def inOrder(self,node):
        if node:
            self.inOrder(node.left)
            print(node.data)
            self.inOrder(node.right)

    def in_order_print(self,root):
        if not root:
            return
        self.in_order_print(root.left)
        print(root.data)
        self.in_order_print(root.right)

    def pre_order_print(self,root):
        if not root:
            return
        print(root.data)
        self.in_order_print(root.left)
        self.in_order_print(root.right)
    
    def preOrder(self,node):
        if node:
            print(node.data)
            self.inOrder(node.left)
            self.inOrder(node.right)

    def postOrder(self,node):
        if node:
            self.inOrder(node.left)
            self.inOrder(node.right)
            print(node.data)

    def printTree(self,node, level=0):
        if not node:
            raise ValueError("EMPTY TREE")
        if node != None:
            self.printTree(node.left, level + 1)
            print(' ' * 4 * level + '-> ' + str(node.data))
            self.printTree(node.right, level + 1)


test = [7,1,5]
newBST = BinaryTree()
root = Node(3)
for num in test:
    newBST.insert(root, Node(num))
# newBST.inOrder(root)
# newBST.preOrder(newBST.root)
# newBST.postOrder(newBST.root)
# newBST.postOrder(newBST.root)
# newBST.printTree(root)
newBST.in_order_print(root)
newBST.pre_order_print(root)




