class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=[]
        for i in nums:
            if i!=0:
                l.append(i)
        nums[:len(l)]=l
        for i in range(len(l),len(nums)):
            nums[i]=0
        

            