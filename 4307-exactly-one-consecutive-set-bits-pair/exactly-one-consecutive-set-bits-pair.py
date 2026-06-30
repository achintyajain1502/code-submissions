class Solution(object):
    def consecutiveSetBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n=bin(n)[2:]
        c=0
        print n
        for i in range(0,len(str(n))-1):
            if n[i]=="1" and n[i+1]=="1":
                c+=1
        if c==1:
            return True
        return False
        