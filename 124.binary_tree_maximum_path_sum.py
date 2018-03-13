# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    max_value = -9999999

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.f(root)
        return self.max_value

    def f(self, node):
        if not node:
            return 0
        left = max(0, self.f(node.left))
        right = max(0, self.f(node.right))
        self.max_value = max(self.max_value, left + right + node.val)
        return max(left, right) + node.val