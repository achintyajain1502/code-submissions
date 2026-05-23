class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n>0):
            n=bin(n)
            if(n[2:].count("1")==1):
                return(True)
            else:
                return(False)
        else:
            return(False)