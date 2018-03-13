# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    last = None

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.

        """
        if not root:
            return
        self.flatten(root.right)
        self.flatten(root.left)
        root.left = None
        root.right = self.last
        self.last = root


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
