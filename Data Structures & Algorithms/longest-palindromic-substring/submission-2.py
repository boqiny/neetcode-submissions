class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for c in range(len(s)):
            for l, r in ((c, c), (c, c + 1)):
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    if r - l + 1 > len(res):
                        res = s[l:r+1]
                    l, r = l - 1, r + 1
        return res