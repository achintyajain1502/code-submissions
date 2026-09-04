class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        l=[]
        i=0
        while i<len(nums):
            o=max(nums[:i+1])-min(nums[i:])
            l.append(o)
            if o<=k:
                return l.index(o)
            i+=1
        return -1