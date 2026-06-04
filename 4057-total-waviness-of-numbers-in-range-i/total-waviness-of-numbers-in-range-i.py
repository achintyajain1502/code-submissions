class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        c=0
        for i in range(num1,num2+1):
            for j in range(1,len(str(i))-1):
                i=str(i)
                if i[j]>i[j+1] and i[j]>i[j-1]:
                    c+=1
                elif i[j]<i[j+1] and i[j]<i[j-1]:
                    c+=1
                else:continue
        return c

       
        