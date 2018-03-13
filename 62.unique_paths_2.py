class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        p = [1] * m
        for i in range(1, n):
            for j in range(1, m):
                p[j] += p[j-1]
        return p[-1]