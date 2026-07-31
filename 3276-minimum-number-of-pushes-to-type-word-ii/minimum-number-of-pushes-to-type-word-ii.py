class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        m={}
        for i in word:
            if i in m:
                m[i]+=1
            else:
                m[i]=1
        l=[]
        for i in m:
            l.append(m[i])
        l.sort(reverse=True)
        i=0
        c=0
        while i<len(l):
            if i<8:
                c+=l[i]
            elif i>=8 and i<16:
                c+=2*l[i]
            elif i>=16 and i<24:
                c+=3*l[i]
            else:
                c+=4*l[i]
            i+=1
        return c        