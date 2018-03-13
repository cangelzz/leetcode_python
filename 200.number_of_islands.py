class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        ROWS = len(grid)
        COLUMNS = len(grid[0])
        islands = 0

        def dfs(r, c):
            if grid[r][c] == '1':
                grid[r][c] = '0'
                if r - 1 >= 0: dfs(r - 1, c)
                if r + 1 < ROWS: dfs(r + 1, c)
                if c - 1 >= 0: dfs(r, c - 1)
                if c + 1 < COLUMNS: dfs(r, c + 1)

        for i in range(ROWS):
            for j in range(COLUMNS):
                if grid[i][j] == '1':
                    islands += 1
                    dfs(i, j)
        return islands
