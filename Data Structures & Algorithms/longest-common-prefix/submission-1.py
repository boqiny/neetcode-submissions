class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(min(map(len, strs))):
            cur = strs[0][i]
            for s in strs[1:]:
                if s[i] != cur:
                    return res
            res += cur
        return res