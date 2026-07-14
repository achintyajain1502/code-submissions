class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        k=[]
        s=0
        for i in range(0,len(nums),2):
            k=nums[i:i+2]
            s+=min(k)
        return s
        