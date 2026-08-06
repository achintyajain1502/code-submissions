class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        for i in range(n,101,1):
            m=1
            k=i
            while i>0:
                m*=i%10
                i//=10
            if m%t==0:
                return k
        

        