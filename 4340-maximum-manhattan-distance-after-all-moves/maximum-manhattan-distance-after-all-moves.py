class Solution(object):
    def maxDistance(self, moves):
        """
        :type moves: str
        :rtype: int
        """        
        l=moves.count("L")
        r=moves.count("R")
        u=moves.count("U")
        d=moves.count("D")
        q=moves.count("_")
        return abs(r-l)+abs(u-d)+q
