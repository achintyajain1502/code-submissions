class Solution:
    def countDigits(self, num: int) -> int:
        c=0
        x=num
        while x:
            if num%(x%10)==0:
                c+=1
                x//=10
            else:
                x//=10
        return c