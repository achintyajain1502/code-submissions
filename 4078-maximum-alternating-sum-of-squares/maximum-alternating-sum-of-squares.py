class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i]<0:
                nums[i]=abs(nums[i])
        nums.sort()
        j=0
        k=len(nums)-1
        l=[]
        i=0
        while i<len(nums) and j<=k:
            if i%2==0:
                l.append(nums[k])
                k-=1
            else:
                l.append(nums[j])
                j+=1
            i+=1
        c=0
        for i in range(len(l)):
            if i%2==0:
                c+=pow(l[i],2)
            else:
                c-=pow(l[i],2)
        return c

