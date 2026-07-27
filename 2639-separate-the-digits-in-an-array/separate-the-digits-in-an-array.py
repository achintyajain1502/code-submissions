class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        def f(n):
            n=str(n)
            for i in range(len(n)):
                ans.append(int(n[i]))
        for i in nums:
            f(i)
        return ans