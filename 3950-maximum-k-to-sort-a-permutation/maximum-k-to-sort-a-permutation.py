class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        l=[]
        k=[]
        for i in range(len(nums)):
            l.append(i)
        for i in range(len(nums)):
            if l[i]!=nums[i]:
                k.append(l[i])
        if k!=[]:
            c=k[0]
            for i in range(1,len(k)):
                c=c&k[i]
            return c
        else:
            return 0