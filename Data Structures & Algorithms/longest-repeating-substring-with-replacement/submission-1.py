class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq = defaultdict(int)
        max_freq = 0
        res = 0
        for r in range(len(s)):
            freq[s[r]] += 1
            max_freq = max(freq.values())
            if r-l+1 - max_freq > k:
                while r-l+1 - max_freq > k:
                    freq[s[l]] -= 1
                    max_freq = max(freq.values())
                    l += 1
            res = max(r-l+1, res)
        return res
