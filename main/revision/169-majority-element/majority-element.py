class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=[]
        k=[]
        for i in nums:
            if i not in k:
                k.append(i)
        for i,num in enumerate(k):
            c.append(nums.count(num))
        index=c.index(max(c))
        return k[index]