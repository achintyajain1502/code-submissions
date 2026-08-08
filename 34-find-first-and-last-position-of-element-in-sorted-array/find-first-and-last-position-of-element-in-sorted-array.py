class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=[-1,-1]
        if target in nums:
            l[0]=nums.index(target)
            nums.reverse()
            l[1]=len(nums)-(nums.index(target)+1)
        return l
        