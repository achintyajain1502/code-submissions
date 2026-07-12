class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        k = sorted(set(arr))
        d = {}
        for i in range(len(k)):
            d[k[i]] = i + 1
        r = []
        for i in arr:
            r.append(d[i])
        return r

