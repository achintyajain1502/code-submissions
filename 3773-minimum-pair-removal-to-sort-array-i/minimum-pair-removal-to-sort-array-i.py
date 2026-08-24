class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        c=0
        while nums!=sorted(nums):
            l=[]
            for i in range(len(nums)-1):
                l.append(nums[i]+nums[i+1])
            m=l.index(min(l))
            nums[m]=min(l)
            del nums[m+1]
            c+=1
        return c