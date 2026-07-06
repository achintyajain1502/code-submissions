class Solution(object):
    def maxDigitRange(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        largest=[]
        smallest=[]
        digit=[]
        for i in nums:
            l=max(str(i))
            s=min(str(i))
            digit.append(int(l)-int(s))
            largest.append(l)
            smallest.append(s)
        m=max(digit)
        for i in range(len(digit)):
            if digit[i]==m:
                c+=nums[i]
        return c

