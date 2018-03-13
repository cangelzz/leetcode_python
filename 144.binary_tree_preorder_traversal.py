class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        r = []
        self.insert(root, r)
        return r

    def insert(self, root, nums):
        if root:
            nums.append(root.val)
            self.insert(root.left, nums)
            self.insert(root.right, nums)


three = TreeNode(3)
two = TreeNode(2)
two.left = three
one = TreeNode(1)
one.right = two
s = Solution()
print(s.preorderTraversal(one))
