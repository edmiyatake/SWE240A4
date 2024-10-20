class Node:
    def __init__(self,val):
        self.val = val
        self.lastName = val[slice(8,33)]
        self.left = None
        self.right = None

def strToASCII(str):
    sum = 0
    # problem was that the first char was not taking precedence
    # as i increases terms in sum should get smaller if divided by i
    for i in range(0,1):
        newSTR = str[slice(8,33)]
        sum += ord(newSTR[i]) + (ord(newSTR[i+1]) * 0.1) + (ord(newSTR[i+2]) * 0.01)
    return sum

str1,str2,i,j = "McKinnen","McLovin",0,0
def compare(str1,str2,i,j):
    # if the first string is less than the second string
    char1 = str1[i]
    char2 = str2[j]

    if char1 < char2:
        return str1
    elif char1 > char2:
        return str2
    else:
        return (compare(str1,str2,i+1,j+1))

# takes in a node and string?
def insert(node,str1):
    if not node:
        return Node(str1)
    sub1 = str1[slice(8,33)]

    if compare(node.lastName, sub1,0,0) == node.lastName:
        node.left = insert(node.left,str1)
    else:
        node.right = insert(node.right,str1)

    # node.height = 1 + max(height(node.left),height(node.right))

    # balance = get_balance(node)

    # if balance > 1 and strToVal(val) < node.left.val:
    #     return right_rotate(node)
    
    # if balance > 1 and strToVal(val) > node.left.val:
    #     node.left = left_rotate(node.left)
    #     return right_rotate(node)
    
    # if balance < -1 and strToVal(val) > node.right.val:
    #     return left_rotate(node)
    
    # if balance < -1 and strToVal(val) < node.right.val:
    #     node.right = right_rotate(node.right)
    #     return left_rotate(node)

    return node

def printTree(node, level=0):
        if node != None:
            printTree(node.left, level + 1)
            print(' ' * 4 * level + '-> ' + str(node.val))
            printTree(node.right, level + 1)

arr1 = []
f = open("fifteen.txt","r")
for line in f:
    arr1.append(line)
f.close()
root = None

for seq in arr1:
    root = insert(root,seq)

printTree(root)


# for element in arr1:
#     print(f"The name is {element[slice(8,33)]} and the corresponding value is: {strToASCII(element)}")
