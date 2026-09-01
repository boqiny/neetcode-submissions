import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = re.sub(r'[^A-Za-z0-9]', '', s)
        i,j = 0, len(clean) - 1
        while i < j:
            if clean[i].lower() != clean[j].lower():
                return False
            i += 1
            j -= 1
        return True

