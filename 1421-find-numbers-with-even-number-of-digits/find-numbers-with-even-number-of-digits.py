class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        for i in nums:
            s=0
            while i>0:
                i%10
                s+=1
                i=i/10
            if s%2==0:
                c+=1
        return c
        