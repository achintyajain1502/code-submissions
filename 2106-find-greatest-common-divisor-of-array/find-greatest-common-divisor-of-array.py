class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=max(nums)
        b=min(nums)
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        return gcd(a,b)
        