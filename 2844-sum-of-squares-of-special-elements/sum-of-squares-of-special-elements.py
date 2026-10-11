class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        c=0
        n=len(nums)
        i=1
        while i<=n:
            if n%i==0:
                c+=pow(nums[i-1],2)
            i+=1
        return c