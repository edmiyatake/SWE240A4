class Node:
    def __init__(self,str):
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
    def choose(self,str):
        if str[0] == "I":
            self.insert(str)
        elif str[0] == "D":
            self.delete(str)
        else:
            raise ValueError("Not a valid operation code")
    
    def insert(self,str):
        # takes in string from file and inserts into tree
        # example input string: "I8599999Zot                      0451WET 1"
        # first check if root exists
        newNode = Node(str)
        if not self.root:
            self.root = newNode
        else:
            # do a comparison with parent node and make sure that the lowest asci goes to left
            if ord(newNode.data[8]) < ord(self.root.data[8]):
                self.root.left
    
    def remove(self,str):
        exit
                

    


# f = open("tree-input.txt","r")
# # instead of trying to insert in the tree i think its better to sort and rewrite the input file
# for line in f:
#     print(line)

# f.close()

