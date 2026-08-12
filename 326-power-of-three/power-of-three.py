class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==0:
            return False
        x=0
        while 3**x<=n:
            if 3**x==n:
                return True
            else:
                x+=1
        return False
        