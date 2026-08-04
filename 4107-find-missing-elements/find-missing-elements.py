class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        l=[]
        i=nums[0]
        j=nums[-1]
        k=0
        while i<j:
            if i!=nums[k]:
                l.append(i)
                i+=1
            else:
                i+=1
                k+=1
        return l
        
