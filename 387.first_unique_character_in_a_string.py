class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = []
        cache = []
        for idx, c in enumerate(s):
            if c in cache:
                continue
            if s.count(c) == 1:
                result.append(idx)
            else:
                cache.append(c)
        if result:
            return result[0]
        else:
            return -1
