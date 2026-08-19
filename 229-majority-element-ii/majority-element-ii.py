class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        m={}
        for i in nums:
            if i in m:
                m[i]+=1
            else:
                m[i]=1
        l=[]
        for i,v in m.items():
            if v>(n/3):
                l.append(i)
        return l