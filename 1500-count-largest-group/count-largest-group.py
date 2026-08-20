class Solution:
    def countLargestGroup(self, n: int) -> int:
        l={}
        for i in range(1,n+1):
            digit_sum = sum(map(int, str(abs(i))))
            if digit_sum in l:
                l[digit_sum]+=1
            else:
                l[digit_sum]=1
        c=max(l.values())
        k=0
        for i in l.values():
            if i==c:
                k+=1
        return k
