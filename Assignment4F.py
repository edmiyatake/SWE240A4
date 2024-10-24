class Node:
    def __init__(self,inputSTR):
        self.inputSTR = inputSTR
        self.op = inputSTR[0]
        self.studentNum = inputSTR[slice(1,8)] # indices 1 -> 7 => 7 elements
        self.lastName = inputSTR[slice(8,33)]
        self.home = inputSTR[slice(33,37)] # indices 33 -> 36 => 4 elements
        self.program = inputSTR[slice(37,41)] # indices 37 -> 40 => 4 elements        
        self.year = inputSTR[slice(41,42)] #indices 41-> 41 => 1 element
        self.left = None
        self.right = None
# input: root node, string from input.txt
class BinaryTree:
    def __init__(self):
        self.root = None

    def root(self):
        return self.root
    
    def height(self,node):
        if not node:
            return 0
        return node.height
        
    def insert(self,inputSTR):

        if self.root == None:
            self.root = Node(inputSTR)
            return

        currNode = self.root
        while currNode:
            if currNode.lastName > inputSTR[slice(8,33)]:
                # if currNode is empty, insert into left
                if not currNode.left:
                    currNode.left = Node(inputSTR)
                    currNode.left.height = 1 + currNode.height
                    return
                else:
                    currNode = currNode.left
            else:
                if not currNode.right:
                    currNode.right = Node(inputSTR)
                    currNode.right.height = 1 + currNode.height
                    return
                else:
                    currNode = currNode.right

    def inOrder(self,node):
        if node:
            self.inOrder(node.left)
            print(node.lastName)
            self.inOrder(node.right)
    
    def preOrder(self,node):
        if not node:
            return 
        print(node.lastName)
        if node.left:
            self.preOrder(node.left)
        if node.right:
            self.preOrder(node.right)

    def postOrder(self,node):
        if not node:
            return 
        if node.left:
            self.postOrder(node.left)
        if node.right:
            self.postOrder(node.right)
        print(node.lastName)
    
    def BFS(self,root):
        queue = [root]
        while queue:
            currNode = queue.pop(0)
            print(currNode.lastName)
            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)

    def printTree(self,node, level=0):
        if node != None:
            self.printTree(node.left, level + 1)
            print(' ' * 4 * level + '-> ' + str(node.lastName))
            self.printTree(node.right, level + 1)

# root = Node("I8534534McKay                    0251CT  1")
# insert("I8400342LaPorte                  0045JA  1")
# insert("I8499120Black                    0341RST 1")

# test = [1,23,45,65,2,32]
# newBST = BinaryTree()
# for num in test:
#     newBST.insert(num)


test1 = []
f = open("fifteen.txt","r")
for line in f:
    test1.append(line)
f.close()

newBST1 = BinaryTree()
for strings in test1:
    newBST1.insert(strings)

# newBST1.printTree(newBST1.root)
print("This is an inOrder traversal")
newBST1.inOrder(newBST1.root)

print("This is an preOrder traversal")
newBST1.preOrder(newBST1.root)

print("This is an postOrder traversal")
newBST1.postOrder(newBST1.root)

print("This is a BFS traversal")
newBST1.BFS(newBST1.root)
