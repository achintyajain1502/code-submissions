class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        x="0"
        sum=0
        for i in str(n):
            if i!="0":
                x+=i
            else:continue
        for i in x:
            sum+=int(i)
        return(int(x)*sum)
            
        