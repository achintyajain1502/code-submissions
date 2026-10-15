class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        c=0
        for i in range(len(nums)):
            s=set()
            for j in range(i,len(nums)):
                s.add(nums[j])
                c+=pow(len(s),2)
        return c               
