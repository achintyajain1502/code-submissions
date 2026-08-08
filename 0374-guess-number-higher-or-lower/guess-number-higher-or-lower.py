# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l=1
        r=n
        while l<=r:
            q=(l+r)//2
            k=guess(q)
            if k==0:
                return q
            elif k==1:
                l=q+1              
            else:
                r=q-1             