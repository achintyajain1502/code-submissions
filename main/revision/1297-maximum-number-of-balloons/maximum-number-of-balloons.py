class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        c=0
        text=list(text)
        while True:
            for i in 'balloon':
                if i not in text:
                    return c
                text.remove(i)
            c+=1