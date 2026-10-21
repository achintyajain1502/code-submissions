class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        k={}
        nums.sort()
        c=1
        l=[]
        n=len(nums)
        for i in nums:
            if str(i) in k:
                k[str(i)]+=1
                l.append(i)
                nums.remove(i)
                break
            else:
                k[str(i)]=1
        for i in range(n-1):
            if nums[i]!=c:
                l.append(c)
                break
            else:
                c+=1
        if len(l)==1:
            l.append(nums[-1]+1)
        return l    