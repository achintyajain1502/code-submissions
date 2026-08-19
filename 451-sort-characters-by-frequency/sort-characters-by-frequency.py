class Solution:
    def frequencySort(self, s: str) -> str:
        m={}
        for i in s:
            if i in m:
                m[i]+=1
            else:
                m[i]=1
        l=[]
        while m:
            k=max(m, key=m.get)
            l.append(k*m[k])
            m.pop(k)
        return "".join(l)