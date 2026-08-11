class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        l=[]
        j=0
        i=1
        k=[]
        while i<n+1:
            if k==target:
                break
            if target[j]==i:
                k.append(i)
                l.append("Push")
                j+=1
                i+=1
            else:
                l.append("Push")
                l.append("Pop")
                i+=1
        return l
        