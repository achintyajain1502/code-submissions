class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while(len(str(num))!=1):
            n=0
            for i in range(len(str(num))):
                n+=num%10
                num//=10
            num=n
        return num