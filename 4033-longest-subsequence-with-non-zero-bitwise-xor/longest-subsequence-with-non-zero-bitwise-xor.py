class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        x=0
        zeros=0
        for i in nums:
            x^=i
            if i==0:
                zeros+=1   
        if x!=0:
            return len(nums)
        if zeros==len(nums):
            return 0
        return (len(nums)-1)