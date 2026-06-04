class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # i=0
        # j=1
        # while i<=len(nums) and j<=len(nums):
        #     if nums[i]+nums[j]==target:
        #         return [i,j]
        #     else:
        #         i+=1
        #         j+=1

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
