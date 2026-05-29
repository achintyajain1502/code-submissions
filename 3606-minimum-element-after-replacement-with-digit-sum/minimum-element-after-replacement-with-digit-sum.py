class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            n=0
            for j in range(len(str(nums[i]))):
                n+=nums[i]%10
                nums[i]//=10
            nums[i]=n
        return(min(nums))
        