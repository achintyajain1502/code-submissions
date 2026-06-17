class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        c=0
        n=len(nums)
        for i in range(len(nums)):
            if nums[i]>nums[(i+1)%n]:
                c+=1
        
        return c<=1
