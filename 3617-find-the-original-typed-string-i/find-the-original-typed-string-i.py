class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        k=0
        for i in range(len(word)-1):
            if word[i]==word[i+1]:
                k+=1
        return k+1

        