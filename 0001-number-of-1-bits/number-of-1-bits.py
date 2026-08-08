class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        b=bin(n)
        b=b[2:]
        # print(type(b))   (string)
        l=0
        for i in range (len(b)):
            if(b[i]=="1"):
                l+=1
        return(l)