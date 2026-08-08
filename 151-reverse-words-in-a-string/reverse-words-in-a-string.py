class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.strip()
        s=s.split(" ")[::-1]
        k=[]
        for i in s:
            if i!="":
                k.append(i)
        return(" ".join(k))
                