class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        l=[]
        i=0
        j=1
        c=1
        while i<j and j<len(s):
            if s[i]==s[j]:
                c+=1
                i+=1
                j+=1
            else:
                l.append(c)
                c=1
                i=j
                j+=1
        l.append(c)
        i=0
        j=1
        c=0
        while j<len(l):
            c+=min(l[i],l[j])
            i+=1
            j+=1
        return c