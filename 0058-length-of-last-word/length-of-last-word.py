class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=s.split(" ")
        k=[]
        for i in l:
            if(i!=""):
                k.append(i)
            else:
                continue
        return(len(k[-1]))


#return len(s.split()[-1]) (more easy way)