class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        c=0
        s=int(s,2)
        while s!=1:
            if s%2!=0:
                s+=1
                c+=1
            else:
                s//=2
                c+=1
        return c
        