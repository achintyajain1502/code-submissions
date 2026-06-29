class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        l=[]
        for i in range(len(words)):
            for j in range(len(words)):
                if j==i:
                    continue
                elif words[i] in words[j]:
                    l.append(words[i])
        return list(set(l))

        