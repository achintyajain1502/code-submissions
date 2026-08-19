class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m={}
        for i in nums:
            if i in m:
                m[i]+=1
            else:
                m[i]=1
        l=[]
        for i in range(k):
            v=max(m,key=m.get)
            l.append(v)
            m.pop(v)
        return l
        