class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            nums[i]=pow(nums[i],2)
        # print(nums)
        # for i in range(len(nums)):
        #     nums[i]=nums[i]**2
        nums.sort()
        return(nums)