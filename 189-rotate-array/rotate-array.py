class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k%=n
        nums.reverse()
        print nums
        nums[:k]=reversed(nums[:k])
        nums[k:]=reversed(nums[k:])


        # for i in range(k): (TLE issue)
        #     temp=nums[-1]
        #     for i in range(-1,-len(nums),-1):
        #         nums[i]=nums[i-1]
        #     nums[0]=temp

