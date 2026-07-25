class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        s="0"
        for i in range(1,n+1):
            s+=bin(i)[2:]
        return int(s,2)%((10**9)+7)
        