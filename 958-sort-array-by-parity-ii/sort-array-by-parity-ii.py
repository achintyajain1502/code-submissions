class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        e=[]
        o=[]
        r=[]
        for i in nums:
            if i%2==0:
                e.append(i)
            else:
                o.append(i)
        i=0
        j=0
        while i<len(e) or j<len(o):
            r.append(e[i])
            r.append(o[j])
            i+=1
            j+=1
        return r
