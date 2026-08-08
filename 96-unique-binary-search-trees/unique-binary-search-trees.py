class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        def fac(n):
            if n==0 or n==1:
                return 1
            else:
                return n*fac(n-1)
        N=fac(2*n)
        D=fac(n+1)*fac(n)
        return N/D
        