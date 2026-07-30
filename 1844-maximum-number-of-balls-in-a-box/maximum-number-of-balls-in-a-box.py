class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        b={}
        for i in range(lowLimit,highLimit+1):
            s=0
            while i>0:
                s+=i%10
                i=i/10
            if s in b:
                b[s]+=1
            else:
                b[s]=1
        return max(b.values())

            
        