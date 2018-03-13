class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        if len(nums) == 1:
            return 1

        max_len = 1
        for i in range(len(nums) - 1):
            cur_len = 1
            last = nums[i]
            for j in range(i + 1, len(nums)):

                if nums[j] > last:
                    cur_len += 1
                    last = nums[j]
            if cur_len > max_len:
                max_len = cur_len

        return max_len


s = Solution()
print(s.lengthOfLIS([10,9,2,5,3,4]))