class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        l=[]
        for i in operations:
            if i=="D":
                l.append(l[-1]*2)
            elif i=="C":
                l.remove(l[-1])
            elif i=="+":
                l.append(l[-1]+l[-2])
            else:
                l.append(int(i))
        return sum(l)