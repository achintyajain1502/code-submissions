class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        k=""
        m=""
        i=0
        l={}
        for t in knowledge:
            l[t[0]]=t[1]
        while i<len(s):
            if s[i]=="(":
                i+=1
                k=""
                while s[i]!=")":
                    k+=s[i]
                    i+=1
                if k not in l:
                    m+="?"
                else:
                    m+=l[k]
            else:
                m+=s[i]
            i+=1
        return m
