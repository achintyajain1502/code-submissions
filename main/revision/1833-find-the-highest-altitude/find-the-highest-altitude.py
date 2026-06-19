class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        alt=[0]
        for i in range(len(gain)):
            alt.append(gain[i]+alt[i])
        return max(alt)
        