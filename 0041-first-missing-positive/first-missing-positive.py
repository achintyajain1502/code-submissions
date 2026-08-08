class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=list(set(nums))
        nums.append(0)
        nums.sort()
        k=nums.index(0)
        nums=nums[k:]
        print k
        print nums
        if len(nums)>=2:
            if nums[0]==0 and nums[1]==0:
                nums=nums[1:]
                print nums
            for i,v in enumerate(nums):
                if i!=v:
                    return i
        return nums[-1]+1


