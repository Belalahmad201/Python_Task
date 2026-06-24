class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# DFS Recursive Approach
def max_depth(root):
    if root is None:
        return 0

    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    return 1 + max(left_depth, right_depth)


# Build Sample Binary Tree
#
#          A
#         / \
#        B   C
#       / \
#      D   E
#     /
#    F
#
# Maximum Depth = 4
#

root = TreeNode("A")
root.left = TreeNode("B")
root.right = TreeNode("C")
root.left.left = TreeNode("D")
root.left.right = TreeNode("E")
root.left.left.left = TreeNode("F")

depth = max_depth(root)

print("Maximum Depth of Binary Tree:", depth)