class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        j=0
        i=-1
        for k in range(len(s)//2):
            s[j],s[i]=s[i],s[j]
            i-=1
            j+=1
        