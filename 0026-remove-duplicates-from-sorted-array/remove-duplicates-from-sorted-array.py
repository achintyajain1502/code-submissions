class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=[]
        for i in range(len(nums)):
            if (nums[i] not in l):
                l.append(int(nums[i]))
        for j in range(len(l)):
            nums[j]=l[j]
        return(len(l))