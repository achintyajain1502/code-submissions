class Solution(object):
    def evenOddBit(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        e=0
        o=0
        n=bin(n)[2:][::-1]
        for i in range(len(n)):
            if n[i]=="1" and i%2==0:
                e+=1
            elif n[i]=="1" and i%2!=0:
                o+=1
        return [e,o]
        