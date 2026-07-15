class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        m=""
        k=list(s)
        i=0
        j=len(s)-1
        while i<=j:
            if k[i].isalpha():
                if k[j].isalpha():
                    k[i],k[j]=k[j],k[i]
                    i+=1
                    j-=1
                else:
                    j-=1
            else:
                i+=1
        for i in k:
            m+=str(i)
        return m


        