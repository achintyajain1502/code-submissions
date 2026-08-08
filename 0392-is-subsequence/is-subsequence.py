class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        j=0
        i=0
        while j<len(t) and i<len(s):
            if t[j]==s[i]:
                i+=1
                j+=1
            elif t[j]!=s[i]:
                j+=1
        return i==len(s)

        