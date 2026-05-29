class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l=""
        for j in range(len(s)):
            l+=str(ord(s[j])-ord('a')+1)
        l=int(l)
        for i in range(k):
            n=0        
            for j in range(len(str(l))):
                n+=l%10
                l//=10
            l=n
        return n