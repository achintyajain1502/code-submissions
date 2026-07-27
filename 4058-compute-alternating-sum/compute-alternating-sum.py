class Solution(object):
    def alternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=0
        for i in range(len(nums)):
            if i%2==0:
                s+=nums[i]
            else:
                s-=nums[i]
        return s
        