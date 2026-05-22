class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        s=1
        if(num==1):
            return(False)
        for i in range(2,int(math.sqrt(num))+1):
            if(num%i==0):
                s+=i
                if (i!=num//i):
                    s+=num//i
        if(s==num):
            return(True)
        else:
            return(False)
            
        