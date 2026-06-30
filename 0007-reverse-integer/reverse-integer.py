class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if(x<0):
            sign=-1
        else:
            sign=1
        x=abs(x)
        n=0
        r=0
        while(x>0):
            r=x%10
            n= n*10+ r
            x//=10
        n=sign*n
        if (-2**31 > n or n >2**31 - 1):
            return(0)
        else:
            return(n)
