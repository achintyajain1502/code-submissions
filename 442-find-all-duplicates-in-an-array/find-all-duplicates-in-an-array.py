class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m={}
        l=[]
        for i in nums:
            if i in m:
                m[i]+=1
            else:
                m[i]=1
        for k,v in m.items():
            if v==2:
                l.append(k)
        return l
        


        