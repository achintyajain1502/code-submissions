class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=[]
        nums=list(set(nums))
        for i in range(3):
            if nums!=[]:
                l.append(max(nums))
                nums.remove(max(nums))
        if len(l)<3:
            return max(l)
        return min(l)
        