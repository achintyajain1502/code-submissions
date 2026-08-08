class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        x=0
        for i in nums:
            x^=i
        return(x)


        # for i in range(len(nums)):
        #     if(nums.count(nums[i])==1):
        #         return(nums[i])