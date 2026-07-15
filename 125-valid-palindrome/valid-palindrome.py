class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        k=""
        s=s.strip()
        for i in s:
            if i.isalnum():
                k+=str(i.lower())
            else:
                continue
        m=k[::-1]
        return k==m
        