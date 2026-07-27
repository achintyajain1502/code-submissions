class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        esum=sum(nums)
        s=0
        for i in nums:
            if len(str(i))>1:
                i=str(i)
                for j in range(len(i)):
                    s+=int(i[j])
            else:
                s+=i
        return abs(esum-s)

        