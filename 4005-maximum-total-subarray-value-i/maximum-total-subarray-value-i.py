class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        m=max(nums)
        mi=min(nums)
        return(k*(m-mi))
        