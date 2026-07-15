class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        k=""
        for i in s:
            if i=="i":
                k=k[::-1]
            else:
                k+=i
        return k
        