class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def no(n):
            s=set()
            while n>0:
                s.add(n%10)
                n//=10
            return s
        k=[]
        for i in range(left,right+1):
            s=no(i)
            if 0 in s:
                continue
            for j in s:
                if i%j!=0:
                    break
            else:
                k.append(i)  
        return k
        