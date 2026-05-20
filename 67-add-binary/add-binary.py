class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if(len(a)>len(b)):
            b="0"*(len(a)-len(b))+b
        if(len(b)>len(a)):
            a="0"*(len(b)-len(a))+a
        c=""
        d=""
        for i in range(-1,-max(len(a),len(b))-1,-1):
            if(a[i]=="0" and b[i]=="0"):
                if(c=="1"):
                    d+="1"
                    c="0"
                else:
                    d+="0"
                    c="0"
            elif(a[i]=="0" and b[i]=="1"):
                if(c=="1"):
                    d+="0"
                    c="1"
                else:
                    d+="1"
                    c="0"
            elif(a[i]=="1" and b[i]=="0"):
                if(c=="1"):
                    d+="0"
                    c="1"
                else:
                    d+="1"
                    c="0"
            elif(a[i]=="1" and b[i]=="1"):
                if(c=="1"):
                    d+="1"
                    c="1"
                else:
                    d+="0"
                    c="1"
        if (c=="1"):
            d+="1"    
        return(d[::-1])

