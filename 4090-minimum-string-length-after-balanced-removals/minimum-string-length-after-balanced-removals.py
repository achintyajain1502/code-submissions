class Solution(object):
    def minLengthAfterRemovals(self, s):
        """
        :type s: str
        :rtype: int
        """
        m={}
        for i in s:
            if i in m:
                m[i]+=1
                
            else:
                m[i]=1
        l=m.values()
        if len(l)==2:
            return abs(l[0]-l[1])
        return l[0]