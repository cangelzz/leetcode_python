class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_sum = max_sum = nums[0]
        for num in nums[1:]:
            cur_sum = max(cur_sum + num, num)
            max_sum = max(max_sum, cur_sum)

        return max_sum

s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
