class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans=[]
        for i in range(n+1):
            c=0
            for j in bin(i)[2:]:
                if j=="1":
                    c+=1
            ans.append(c)
        return ans