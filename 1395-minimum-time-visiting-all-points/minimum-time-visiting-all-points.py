class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        c=0
        for i in range(len(points)-1):
            dx=abs(points[i+1][0]-points[i][0])
            dy=abs(points[i+1][1]-points[i][1])
            c+=max(dx,dy)
        return c