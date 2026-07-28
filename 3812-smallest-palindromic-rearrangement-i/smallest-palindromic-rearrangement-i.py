class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = Counter(s)

        left = []
        mid = ""

        for ch in "abcdefghijklmnopqrstuvwxyz":
            left.append(ch * (cnt[ch] // 2))
            if cnt[ch] % 2:
                mid = ch

        left = "".join(left)
        return left + mid + left[::-1]