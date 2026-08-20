class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        m={}
        for i in nums:
            if i in m:
                return i
            else:
                m[i]=1