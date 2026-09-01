class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = set(s)
        res = 0
        print(charSet)
        for c in charSet:
            l, count = 0, 0
            for r in range(len(s)):
                if s[r] != c:
                    count += 1
                if count > k:
                    while count > k:
                        if s[l] != c:
                            count -= 1
                        l += 1
                res = max(res, r-l+1)
        return res

