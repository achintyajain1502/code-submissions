class Solution(object):
    def isPalindromic(self, s):
        """
        :type s: str
        :rtype: bool
        """
        k=[]
        for i in s:
            k.append(bin(ord(i))[2:].zfill(8))
        l="".join(k)
        return l==l[::-1]

