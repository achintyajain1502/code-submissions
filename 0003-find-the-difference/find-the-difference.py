class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        k=0
        l=0
        for i in s:
            k+=ord(i)
        for i in t:
            l+=ord(i)
        return chr(l-k)
