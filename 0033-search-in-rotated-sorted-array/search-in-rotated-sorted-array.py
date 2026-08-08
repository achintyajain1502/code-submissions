class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return(nums.index(target))
        else:
            return -1
        # l=0
        # r=len(nums)
        # while l<=r:
        #     q=(l+r)//2
        #     if(nums[q]==target):
        #         return q
        #     elif(target>nums)
        