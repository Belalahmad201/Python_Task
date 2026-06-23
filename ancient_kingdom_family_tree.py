class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Recursive Inorder Traversal
def inorder_recursive(node, result):
    if node:
        inorder_recursive(node.left, result)
        result.append(node.value)
        inorder_recursive(node.right, result)


# Iterative Inorder Traversal
def inorder_iterative(root):
    stack = []
    result = []
    current = root

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        result.append(current.value)
        current = current.right

    return result


# Build Binary Tree
#
#         A
#       /   \
#      B     C
#     / \   / \
#    D   E F   G
#
root = TreeNode("A")
root.left = TreeNode("B")
root.right = TreeNode("C")
root.left.left = TreeNode("D")
root.left.right = TreeNode("E")
root.right.left = TreeNode("F")
root.right.right = TreeNode("G")

# Recursive Traversal
recursive_result = []
inorder_recursive(root, recursive_result)

# Iterative Traversal
iterative_result = inorder_iterative(root)

print("Recursive Inorder Traversal:", " -> ".join(recursive_result))
print("Iterative Inorder Traversal:", " -> ".join(iterative_result))