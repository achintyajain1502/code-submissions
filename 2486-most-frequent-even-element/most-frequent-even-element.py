class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        m={}
        for i in nums:
            if i%2==0 and i in m:
                m[i]+=1
            elif i%2==0 and i not in m:
                m[i]=1
        m=dict(sorted(m.items()))
        if m!={}:
            k=max(m,key=m.get)
            return k
        else:
            return -1