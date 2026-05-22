class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        f=0
        if(digits.count(9)==len(digits)):
            f=1
        for i in range(len(digits)-1,-1,-1):
            if(digits[i]==9):
                digits[i]=0
            else:
                digits[i]+=1
                break
        if(f==1):
            digits=[1]+digits
        return(digits)
