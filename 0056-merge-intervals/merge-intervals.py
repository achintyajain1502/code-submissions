class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        k=[intervals[0]]
        for i in range(1,len(intervals)):
            if k[-1][0]<=intervals[i][0] and intervals[i][0]<=k[-1][1]:
                k[-1][1]=max(k[-1][1],intervals[i][1])
            else:
                k.append(intervals[i])
        return k