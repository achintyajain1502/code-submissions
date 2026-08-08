class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n<=0):
            return False
        for i in [2,3,5]:
            while n%i==0:
                n//=i
        if(n==0 or n==1):
            return(True)
        else:
            return(False)        