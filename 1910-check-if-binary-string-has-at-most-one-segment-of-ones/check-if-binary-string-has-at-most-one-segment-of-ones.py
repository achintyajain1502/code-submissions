class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i=1
        while i<len(s):
            if s[i]=="0":
                for j in range(i,len(s)):
                    if s[j]=="1":
                        return False
            i+=1
        return True

        