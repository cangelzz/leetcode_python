class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        ROWS = len(image)
        COLUMNS = len(image[0])
        color = image[sr][sc]
        if color == newColor:
            return image

        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor

                if r - 1 >= 0: dfs(r - 1, c)
                if r + 1 < ROWS: dfs(r + 1, c)
                if c - 1 >= 0: dfs(r, c - 1)
                if c + 1 < COLUMNS: dfs(r, c + 1)

        dfs(sr, sc)
        return image