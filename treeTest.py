class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def root(self):
        return self.root
        
    def insert(self,val):

        if self.root == None:
            self.root = Node(val)
            return

        currNode = self.root
        while currNode:
            if currNode.data > val:
                # if currNode is empty, insert into left
                if not currNode.left:
                    currNode.left = Node(val)
                    return
                else:
                    currNode = currNode.left
            else:
                if not currNode.right:
                    currNode.right = Node(val)
                    return
                else:
                    currNode = currNode.right

    def inOrder(self,node):
        if node:
            self.inOrder(node.left)
            print(node.data)
            self.inOrder(node.right)
    
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

test = [1,23,45,65,2,32]
newBST = BinaryTree()
for num in test:
    newBST.insert(num)
print(newBST.root)
# newBST.inOrder(newBST.root)
newBST.preOrder(newBST.root)
# newBST.postOrder(newBST.root)




