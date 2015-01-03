__author__ = 'ryan'

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        # recursive function
        # add one to min depth of children
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 1
        elif root.left is None and root.right is not None:
            return 1 + self.minDepth(root.right)
        elif root.left is not None and root.right is None:
            return 1 + self.minDepth(root.left)
        else:
            return min(1 + self.minDepth(root.right), 1 + self.minDepth(root.left))