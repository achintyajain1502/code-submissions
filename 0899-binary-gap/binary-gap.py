class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        l=[]
        ans=0
        n=bin(n)[2:]
        print n
        for i in range(len(n)):
            if (n[i]=="1"):
                l.append(i)
        for i in range(1,len(l)):
            ans=max(ans,l[i]-l[i-1])
        return(ans)

        # n=bin(n)[2:]
        # k=n.find("1")
        # n=n[k+1:]
        # m=n.find("1")
        # return(m+1-k))