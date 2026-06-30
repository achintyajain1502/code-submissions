class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        ans=0
        for i in columnTitle:
            ans=ans*26+(ord(i)-ord("A")+1)
        return ans

