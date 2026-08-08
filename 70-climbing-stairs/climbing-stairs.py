class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        m={}
        def way(n):
            if n==0:
                return 1
            if n<0:
                return 0
            
            if n in m:
                return m[n]
            m[n]=way(n-1)+way(n-2)
            return m[n]
        return way(n)