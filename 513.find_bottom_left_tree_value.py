class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [root]
        result = root.val
        while any(queue):
            result = queue[0].val
            queue = [leaf for node in queue for leaf in (node.left, node.right) if leaf]
        return result