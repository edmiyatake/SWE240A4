# SET AVL IMPLEMENTATION FROM MIT WEBSITE
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

# class BinarySearchTree:
#     def __init__(self):
#         self.root = None
    
def height(node):
    if not node:
        return 0
    return node.height
    
def get_balance(node):
        if node is None:
            return 0
        return height(node.left) - height(node.right)
    
def right_rotate(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    y.height = 1 + max(height(y.left),height(y.right))
    x.height = 1 + max(height(x.left),height(x.right))
    return x

def left_rotate(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    x.height = 1 + max(height(x.left),height(x.right))
    y.height = 1 + max(height(y.left),height(y.right))
    return y

def insert(node,val):
    if not node:
        return Node(val)
    
    if val < node.val:
        node.left = insert(node.left,val)
    else:
        node.right = insert(node.right,val)

    node.height = 1 + max(height(node.left),height(node.right))

    balance = get_balance(node)
    print(balance)

    if balance > 1 and val < node.left.val:
        return right_rotate(node)
    
    if balance > 1 and val > node.left.val:
        node.left = left_rotate(node.left)
        return right_rotate(node)
    
    if balance < -1 and val > node.right.val:
        return left_rotate(node)
    
    if balance < -1 and val < node.right.val:
        node.right = right_rotate(node.right)
        return left_rotate(node)

    return node

def getMinNode(node):
    currNode = node
    while currNode.left:
        currNode = currNode.left
    return currNode

def delete(node,val):
    if not node:
        return node
    elif val < node.val:
        node.left = delete(node.left,val)
    elif val > node.val:
        node.right = delete(node.right, val)
    else:
        if not node.left:
            temp = node.right
            node = None
            return temp
        elif not node.right:
            temp = node.left
            node = None
            return temp
        temp = getMinNode(node.right)
        node.val = temp.val
        node.right = delete(node.right, temp.val)
    
    if not node:
        return node

    node.height = 1 + max(height(node.left),height(node.right))

    balance = get_balance(node)

    if balance > 1 and val < node.left.val:
        return right_rotate(node)
    
    if balance > 1 and val > node.left.val:
        node.left = left_rotate(node.left)
        return right_rotate(node)
    
    if balance < -1 and val > node.right.val:
        return left_rotate(node)
    
    if balance < -1 and val < node.right.val:
        node.right = right_rotate(node.right)
        return left_rotate(node)

    return node
    

def printTree(node, level=0):
        if node != None:
            printTree(node.left, level + 1)
            print(' ' * 4 * level + '-> ' + str(node.val))
            printTree(node.right, level + 1)




# Create an instance of an AVL tree and test insertion
root = None

# Test Case 1: Simple insertion
values_to_insert = [10, 20, 30, 40, 55, 26]
for value in values_to_insert:
    root = insert(root, value)

root = delete(root, 30)
printTree(root)
# Test Case 5: Delete and check rebalancing
