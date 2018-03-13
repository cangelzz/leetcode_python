# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        r = []
        self.insert(root, r)
        return r

    def insert(self, root, nums):
        if root:
            self.insert(root.left, nums)
            self.insert(root.right, nums)
            nums.append(root.val)
