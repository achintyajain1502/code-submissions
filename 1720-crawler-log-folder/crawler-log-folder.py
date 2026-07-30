class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        c=0
        for i in logs:
            if i=="../" and c!=0:
                c-=1
            elif i=="./" or (i=="../" and c==0):
                continue
            else:
                c+=1
        return c
        