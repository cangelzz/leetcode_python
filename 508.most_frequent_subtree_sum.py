# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        import collections
        if root == None: return []

        def calc_sum(node):
            if node == None: return 0
            s = node.val + calc_sum(node.left) + calc_sum(node.right)
            c[s] += 1
            return s

        c = collections.Counter()
        calc_sum(root)
        frequent = max(c.values())
        return [s for s in c.keys() if c[s] == frequent]
