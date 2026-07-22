class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k={}
        for i in nums:
            if i in k:
                k[i]+=1
            else:
                k[i]=1
        for v in k:
            if k[v]==1:
                return v
        