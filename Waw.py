from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = Node("G")
root.left = Node("R")
root.right = Node("O1")
root.left.left = Node("O2")
root.left.right = Node("K1")
root.right.right = Node("K2")


def bfs(root):
    if root is None:
        return []

    q = deque()
    q.append(root)
    ans = []

    while q:
        curr = q.popleft()
        ans.append(curr.val)

        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)

    return ans


def preorder(node):
    if node is None:
        return []
    return [node.val] + preorder(node.left) + preorder(node.right)


def inorder(node):
    if node is None:
        return []
    return inorder(node.left) + [node.val] + inorder(node.right)


def postorder(node):
    if node is None:
        return []
    return postorder(node.left) + postorder(node.right) + [node.val]


print("Tree BFS:", bfs(root))
print("Tree Preorder:", preorder(root))
print("Tree Inorder:", inorder(root))7