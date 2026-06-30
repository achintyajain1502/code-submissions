class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l=0
        r=len(nums)-1
        while l<=r:
            q=(l+r)//2
            if(nums[q]==target):
                return q
            elif(target<nums[q]):
                r=q-1
            else:
                l=q+1
        else:
            return(-1)


        # if target not in nums:
        #     return(-1)
        # else:
        #     return(nums.index(target))   
        