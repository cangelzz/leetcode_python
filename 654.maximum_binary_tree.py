# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        if not nums:
            return None

        m = max(nums)
        idx = nums.index(m)
        node = TreeNode(m)
        if idx > 0:
            node.left = self.constructMaximumBinaryTree(nums[:idx])
        if idx + 1 < len(nums):
            node.right = self.constructMaximumBinaryTree(nums[idx + 1:])
        return node


nums = [3, 2, 1, 6, 0, 5]
s = Solution()
tree = s.constructMaximumBinaryTree(nums)
values = [tree.val == 6, tree.left.val == 3, tree.right.val == 5, tree.left.right.val == 2, tree.left.right.right.val == 1, tree.right.left.val == 0]
print(values)
print([tree.val, tree.left.val, tree.right.val, tree.left.right.val, tree.left.right.right.val, tree.right.left.val])
