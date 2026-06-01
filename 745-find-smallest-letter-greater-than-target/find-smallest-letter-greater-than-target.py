class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        t=ord(target)
        for i in letters:
            if(ord(i)>t):
                return i
        return letters[0]
