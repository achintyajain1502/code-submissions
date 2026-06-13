class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        l=[]
        s=""
        for i in range(26):
            l.append(chr(97+i))
        for i in words:
            k=0
            for j in i:
                k+=weights[ord(j)-ord('a')]
            k%=26
            s+=l[-k-1]
        return s

        