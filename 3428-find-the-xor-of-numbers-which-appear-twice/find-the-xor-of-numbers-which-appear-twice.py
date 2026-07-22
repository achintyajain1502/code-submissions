class Solution(object):
    def duplicateNumbersXOR(self, nums):
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
        l=0
        for i in k:
            if k[i]==2:
                l^=i
        return l

            
        