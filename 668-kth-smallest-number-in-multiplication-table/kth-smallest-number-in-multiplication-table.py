class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        l = 1
        r = m * n
        while l < r:
            mid = (l + r) // 2
            c=0
            for i in range(1, m + 1):
                c+= min(mid // i, n)
            if c<k:
                l = mid + 1
            else:
                r = mid
        return l
