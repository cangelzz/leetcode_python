# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.

        """
        root = self.f2(root)

    def f2(self, root):
        if not root:
            return root

        left = root.left
        if left:
            right_end = left.right
            if not right_end:
                right_end = left

            while right_end.right:
                right_end = right_end.right

            right_end.right = root.right
            root.right = left
            root.left = None

        root.right = self.f2(root.right)
        return root


s = Solution()
three = TreeNode(3)
four = TreeNode(4)
six = TreeNode(6)
two = TreeNode(2)
two.left = three
two.right = four
five = TreeNode(5)
five.right = six
one = TreeNode(1)
one.left = two
one.right = five
f = s.flatten(one)
for i in range(6):
    print(one.val)
    one = one.right
