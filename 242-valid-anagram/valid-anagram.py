class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m={}
        p={}
        for i in s:
            if i in m:
                m[i]+=1
            else:
                m[i]=1
        for i in t:
            if i in p:
                p[i]+=1
            else:
                p[i]=1
        return m==p
        