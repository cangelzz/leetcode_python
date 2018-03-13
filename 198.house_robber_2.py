class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # DP. store state of prev house robbed vs not robbed

        robbed = 0
        not_robbed = 0

        for num in nums:
            robbed, not_robbed = not_robbed + num, max(not_robbed, robbed)

        return max(robbed, not_robbed)