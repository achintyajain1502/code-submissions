class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        m=""
        k=list(str(s))
        l=["a","e","i","o","u"]
        i=0
        j=len(k)-1
        while i<=j:
            if k[i].lower() in l:
                if k[j].lower() in l:
                    k[i],k[j]=k[j],k[i]
                    i+=1
                    j-=1
                else:
                    j-=1
            else:
                i+=1
        for i in k:
            m+=i
        return m



        