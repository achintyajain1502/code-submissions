class Solution(object):
    def haveConflict(self, event1, event2):
        """
        :type event1: List[str]
        :type event2: List[str]
        :rtype: bool
        """
        l=[event1,event2]
        l.sort()
        if l[0][0]<=l[1][0] and l[1][0]<=l[0][1]:
            return True
        return False
        