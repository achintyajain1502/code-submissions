class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        l=[]
        f=-1
        r=-1
        for i in range(1,n+1):
            f+=1
            l.append(i)
        r=0
        while len(l)>1:
            for i in range(k-1):
                r+=1
            r%=len(l)
            del l[r]
        return l[-1]