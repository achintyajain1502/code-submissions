class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=max(nums)
        if n==1 or n==2:
            return n
        else:
            n=len(bin(n)[2:])
            return 2**n

        