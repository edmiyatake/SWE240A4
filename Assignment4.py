class Node:
    def __init__(self,str):
        self.op = str[0]
        self.studentNum = str[slice(1,8)] # indices 1 -> 7 => 7 elements
        self.lastName = str[slice(8,33)] # indices 8 -> 32 => 25 elements
        self.home = str[slice(33,37)] # indices 33 -> 36 => 4 elements
        self.program = str[slice(37,41)] # indices 37 -> 40 => 4 elements
        self.year = str[slice(41,42)] #indices 41-> 41 => 1 element
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        # self.size = 0 

    def choose(self,str):
        if self.op == "I":
            self.insert(str)
        elif self.op == "D":
            self.delete(str)
        else:
            raise ValueError("Not a valid operation code")
    
    def insert(self,str):
        # takes in string from file and inserts into tree
        # example input string: "I8599999Zot                      0451WET 1"
        # first check if root exists
        if not self.root:
            self.root = Node(str)
            return
        currNode = self.root
        while currNode:
            if currNode.lastName > str[slice(8, 33)]:
                if not currNode.left:
                    currNode.left = Node(str)
                    break
                else:
                    currNode = currNode.left
            else:
                if not currNode.right:
                    currNode.right = Node(str)
                    break
                else:
                    currNode = currNode.right
    
    def remove(self,str):
        exit
                
newBST = BST()
f = open("tree-input.txt","r")
for line in f:
    newBST.insert(line)
f.close()

print(newBST.root.lastName)
print(newBST.root.left.lastName)
print(newBST.root.left.left.lastName)
