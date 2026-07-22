class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        k={}
        for i in nums:
            if i in k:
                k[i]+=1
            else:
                k[i]=1
        l=[]
        for i in k:
            if k[i]==1:
                l.append(i)
        return l
        