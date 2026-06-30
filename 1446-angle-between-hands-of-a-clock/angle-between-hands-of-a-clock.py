class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        minangle=minutes*6
        hrangle=(hour%12)*30+minutes*0.5
        diff=abs(hrangle-minangle)
        return min(diff,360-diff)