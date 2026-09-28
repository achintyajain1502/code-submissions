class Solution:
    def reverseParentheses(self, s: str) -> str:
        t=[]
        r=""
        for i in s:
            if i !=")":
                t.append(i)
            else:
                while t[-1]!="(":
                    r+=t.pop()
                t.pop()
                t.extend(r)
                r=""
        return "".join(t)