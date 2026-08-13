class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m=""
        i=0
        j=0
        while i<=len(word1) and j<=len(word2):
            if i==len(word1):
                m+=word2[j:]
                break
            elif j==len(word2):
                m+=word1[i:]
                break
            else:
                m+=word1[i]
                i+=1
                m+=word2[j]
                j+=1
        return (m)
        