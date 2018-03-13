# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        sub = max(self.longestUnivaluePath(root.left), self.longestUnivaluePath(root.right))
        return max(sub, self.go(root.left, root.val) + self.go(root.right, root.val))

    def go(self, node, val):
        if not node or node.val != val:
            return 0

        return 1 + max(self.go(node.left, val), self.go(node.right, val))