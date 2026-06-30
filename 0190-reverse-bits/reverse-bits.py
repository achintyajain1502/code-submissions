class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        n=bin(n)
        l=n[2:]
        l=l.zfill(32)[::-1]
        return(int(l,2))
        