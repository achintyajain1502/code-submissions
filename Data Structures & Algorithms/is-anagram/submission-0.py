class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m1={}
        m2={}
        def fn(s,m):
            for i in s:
                if i in m:
                    m[i]+=1
                else:
                    m[i]=1
            return m
        m1=fn(s,m1)
        m2=fn(t,m2)
        return m1==m2      