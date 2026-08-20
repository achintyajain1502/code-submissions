class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        l={}
        k=[]
        for i in range(left,right+1):
            i=bin(i)[2:]
            k.append(i.count("1"))
        for i in k:
            if i in l:
                l[i]+=1
            else:
                l[i]=1
        r=0
        for i in l.keys():
            c=2
            while c<i:
                if i%c==0:
                    break
                else:
                    c+=1
            if c==i:
                r+=l[i]
        return r
             