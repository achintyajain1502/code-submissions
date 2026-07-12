class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        r=[]
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                r.append(nums[i]*2)
                nums[i+1]=0 
            else:
                r.append(nums[i])  
        r.append(nums[-1])   
        i=0
        j=len(r)
        while i<j:
            if r[i]==0:
                r.remove(r[i])
                r.append(0)
            i+=1
        return r