class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = [0] * 26
        target = [0] * 26
        for c in s1:
            target[ord(c) - ord('a')] += 1
        l = 0
        for r in range(len(s2)):
            window[ord(s2[r])-ord('a')] += 1
            if r-l+1 > len(s1):
                window[ord(s2[l])-ord('a')] -= 1
                l += 1
            if target == window:
                return True
        return False