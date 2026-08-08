class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2!=0:
            return False
        else:
            l=[]
            for i in range(len(s)):
                if s[i]=="(" or s[i]=="{" or s[i]=="[":
                    l.append(s[i])
                elif s[i]==")":
                    if not l or l[-1]!="(":
                        return False
                    l.pop()
                elif  s[i]=="}":
                    if not l or l[-1]!="{":
                        return False
                    l.pop()
                elif s[i]=="]":
                    if not l or l[-1]!="[":
                        return False
                    l.pop()
            return l==[]



        