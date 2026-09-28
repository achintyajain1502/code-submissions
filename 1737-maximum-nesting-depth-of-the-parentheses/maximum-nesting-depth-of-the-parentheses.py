class Solution:
    def maxDepth(self, s: str) -> int:
        c=0
        l=[]
        for i in s:
            if i=="(":
                c+=1
                l.append(c)
            elif i==")":
                c-=1
                l.append(c)
            else:
                l.append(0)
        return max(l)