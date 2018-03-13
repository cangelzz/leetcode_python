class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen = 0
        curlen = 0
        from collections import deque
        d = deque([])
        for char in s:
            if char not in d:
                d.append(char)
                curlen += 1
            else:
                maxlen = max(maxlen, curlen)
                try:
                    while d.popleft() != char:
                        pass
                except IndexError:
                    pass
                d.append(char)
                curlen = len(d)

        return max(maxlen, curlen)