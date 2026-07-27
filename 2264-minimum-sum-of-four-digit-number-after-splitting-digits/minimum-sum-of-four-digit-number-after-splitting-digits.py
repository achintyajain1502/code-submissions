class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        num=list(str(num))
        new1=""
        new2=""

        def fn(n,num):
            n+=min(num)
            num.remove(min(num))
            n+=max(num)
            num.remove(n[-1])
            return n
        new1=int(fn(new1,num))
        new2=int(fn(new2,num))
        return new1+new2
        
        


        