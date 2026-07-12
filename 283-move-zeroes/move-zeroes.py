class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=0
        j=len(nums)
        while i<=j-1:
            if nums[i]==0:
                nums.remove(0)
                nums.append(0)
            i+=1
        