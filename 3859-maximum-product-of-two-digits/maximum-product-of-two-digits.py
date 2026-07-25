class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        n=list(str(n))
        n.sort()
        return int(n[-1])*int(n[-2])
