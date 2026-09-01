from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count_dict = defaultdict(list)
        for word in strs:
            word_count = [0] * 26
            for c in word:
                word_count[ord(c)-ord('a')] += 1
            count_dict[str(word_count)].append(word)

        return list(count_dict.values())
            
            