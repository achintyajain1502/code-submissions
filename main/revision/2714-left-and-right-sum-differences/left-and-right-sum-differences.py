class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer=[]
        leftsum=[]
        rightsum=[]
        for i in range(len(nums)):
            leftsum.append(sum(nums[:i]))
            rightsum.append(sum(nums[i+1:]))
        for i in range(len(nums)):
            answer.append(abs(leftsum[i] - rightsum[i]))
        return answer