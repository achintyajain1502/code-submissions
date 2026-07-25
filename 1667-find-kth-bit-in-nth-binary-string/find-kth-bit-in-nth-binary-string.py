class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        s=["0"]
        def invert(w):
            w=list(w)
            for i in range(len(w)):
                if w[i]=="1":
                    w[i]="0"
                else:
                    w[i]="1"
            return "".join(w)
        for i in range(2,n+1):
            s.append(s[-1]+"1"+invert(s[-1])[::-1])
        return s[-1][k-1]

