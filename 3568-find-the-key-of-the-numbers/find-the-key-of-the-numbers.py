class Solution(object):
    def generateKey(self, num1, num2, num3):
        """
        :type num1: int
        :type num2: int
        :type num3: int
        :rtype: int
        """
        s=""
        num1=str(num1)
        num2=str(num2)
        num3=str(num3)
        def fn(num):
            if len(num)<4:
                num="0"*(4-len(num))+num
            return num
        num1=fn(num1)
        num2=fn(num2)
        num3=fn(num3)
        i=0
        while i<4:
            s+=min(num1[i],num2[i],num3[i])
            i+=1
        return int(s)