class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        l=set()
        for i in range(len(intervals)):
            for j in range(len(intervals)):
                if i!=j and intervals[j][0]<=intervals[i][0] and intervals[i][1]<=intervals[j][1]:
                    l.add(i)
        return len(intervals)-len(l)