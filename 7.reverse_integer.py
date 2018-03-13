class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = int("".join(reversed(str(abs(x)))))
        if num > 2 ** 31: return 0
        if x >= 0:
            return num
        else:
            return -num
