class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        width = len(obstacleGrid[0])
        p = [0] * width
        p[0] = 1
        for row in obstacleGrid:
            for j in range(len(row)):
                if row[j] == 1:
                    p[j] = 0
                elif j > 0:
                    p[j] += p[j - 1]

        return p[-1]