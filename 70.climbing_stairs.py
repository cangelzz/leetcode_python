class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n

        a, b, result = 1, 2, 0

        for i in range(3, n+1):
            result = a + b
            a, b = b, result

        return result