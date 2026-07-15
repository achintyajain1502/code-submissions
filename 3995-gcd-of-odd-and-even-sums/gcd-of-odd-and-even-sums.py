class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        e=2
        o=1
        even=0
        odd=0
        for i in range(n):
            even+=e
            odd+=o
            e=e+2
            o=o+2
        print even
        print odd
        while even:
            odd,even=even,odd%even
        return odd
