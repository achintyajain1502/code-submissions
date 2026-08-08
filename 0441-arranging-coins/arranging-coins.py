class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        i=1
        while n>=i:
            n-=i
            i+=1
            count+=1
        return count       