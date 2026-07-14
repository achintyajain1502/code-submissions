class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        l=[]
        for i in nums:
            l.append(int(i))
        l.sort()
        return str(l[-k])
        