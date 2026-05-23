class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        n=bin(n)
        l=n[2:]
        l=l.zfill(32)[::-1]
        # l=[]
        # for i in range(-1,-33,-1):
        #     l.append(int(n[i]))
        return(int(l,2))
        