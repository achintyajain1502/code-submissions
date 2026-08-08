class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        m={}
        for i in stones:
            if i in m:
                m[i]+=1
            else:
                m[i]=1
        s=0
        for i in m:
            if i in jewels:
                s+=m[i]
        return s
        