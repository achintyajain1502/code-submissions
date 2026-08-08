class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        k=[]
        s=s.split(" ")
        for i in s:
            k.append(i[::-1])
        return " ".join(k)