class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    return root

def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

letters = ['A', 'N', 'G', 'E', 'L']
root = None
for letter in letters:
    root = insert(root, letter)

print("Pre-Order  : ", end="")
preorder(root)
print("\nIn-Order   : ", end="")
inorder(root)
print("\nPost-Order : ", end="")
postorder(root)
print()