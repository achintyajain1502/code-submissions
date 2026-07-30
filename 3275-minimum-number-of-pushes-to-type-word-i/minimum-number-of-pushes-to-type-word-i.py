class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        res=0
        n=len(word)
        for i in range(n):
            res+=(i//8 + 1)
        return res
       