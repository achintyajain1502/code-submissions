class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=nums[0]
        k=0
        if len(nums)==1:
            return nums[0]+1
        for i in range(len(nums)):
            if c==nums[i]:
                k+=c
                c+=1
                print k
            else:
                if k not in nums:
                    return k
                else:
                    while k in nums:
                        k+=1
                    return k
        return k
