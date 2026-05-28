class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        l=0
        word=set(word)
        print word
        for i in word:
            if i.isupper():
                continue
            elif i.upper() in word:
                l+=1
        return l

        