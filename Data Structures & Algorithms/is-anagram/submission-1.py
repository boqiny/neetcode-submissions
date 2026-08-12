from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter1, counter2 = Counter(s), Counter(t)
        return counter1 == counter2
