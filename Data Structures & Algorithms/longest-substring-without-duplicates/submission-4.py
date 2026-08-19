class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        exist = set()
        max_len = 0
        left, right = 0, 0
        while right < len(s):
            # zxyx
            if s[right] in exist:
                while s[left] != s[right]:
                    exist.remove(s[left])
                    left += 1
                left += 1
            else:
                exist.add(s[right])
            # print(right, exist)
            max_len = max(max_len, right-left+1)
            right += 1
        return max_len
