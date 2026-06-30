class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        last = {'a': -1, 'b': -1, 'c': -1}
        ans = 0
        for i in range(len(s)):
            last[s[i]] = i
            ans += min(last['a'], last['b'], last['c']) + 1
        return ans