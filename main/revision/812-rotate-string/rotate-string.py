class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        result=s+s
        if len(s)==len(goal):
            if goal in result:
                return True
        return False
        