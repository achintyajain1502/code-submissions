class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        total=0
        minsum=0
        for i in nums:
            total+=i
            minsum=min(minsum,total)
        return 1-minsum