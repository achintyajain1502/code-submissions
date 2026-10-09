class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        else:
            x=0
            while pow(3,x)<=n:
                if 3**x==n:
                    return True
                else:
                    x+=1
            return False
