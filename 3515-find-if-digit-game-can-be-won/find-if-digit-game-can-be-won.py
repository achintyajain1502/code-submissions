class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s1=0
        s2=0
        for i in nums:
            if 10<=i<=99:
                s2+=i
            else:
                s1+=i
        if s1>s2 or s2>s1:
            return True
        return False        