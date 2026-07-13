class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

tnode2 = TreeNode(20, TreeNode(15), TreeNode(7))
tnode1 = TreeNode(3, TreeNode(9), tnode2)

def preorder(node):
    if not node:
        return []
    return [node.value] + preorder(node.left) + preorder(node.right)

def inorder(node):
    if not node:
        return []
    return inorder(node.left) + [node.value] + inorder(node.right)

def postorder(node):
    if not node:
        return []
    return postorder(node.left) + postorder(node.right) + [node.value]

print(postorder(tnode1))
