from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list[str])
        for s in strs:
            char_count: list[int] = [0] * 26
            for c in s:
                char_count[ord(c) - ord('a')] += 1
            group[str(char_count)].append(s)
            
        return list(group.values())

        