class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        k=1
        ans=1
        for i in range(1,len(word)):
            if word[i]==word[i-1]:
                k+=1
            else:
                ans+=k-1
                k=1
        ans+=k-1
        return ans

        