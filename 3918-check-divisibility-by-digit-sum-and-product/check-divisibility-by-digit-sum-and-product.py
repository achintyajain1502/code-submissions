class Solution:
    def checkDivisibility(self, n: int) -> bool:
        n=str(n)
        s=0
        p=1
        for i in n:
            s+=int(i)
            p*=int(i)
        return int(n)%(s+p)==0
        
            