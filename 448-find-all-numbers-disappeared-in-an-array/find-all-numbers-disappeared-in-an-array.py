class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        # l=[]
        # c=1
        # n=len(nums)
        # nums=list(set(nums))
        # for i in range(n):
        #     if c in nums:
        #         c+=1
        #     else:
        #         l.append(c)
        #         c+=1
        # return l
        s=set(nums)
        l=[]
        for i in range(1,len(nums)+1):
            if i not in s:
                l.append(i)
        return l