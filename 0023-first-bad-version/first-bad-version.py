# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l=1
        r=n
        while l<=r:
            q=(l+r)//2
            if isBadVersion(q)==True:
                r=q
                if isBadVersion(q-1)==False:
                    return q
            elif isBadVersion(q)==False:
                l=q   
                if isBadVersion(q+1)==True:
                    return q+1
