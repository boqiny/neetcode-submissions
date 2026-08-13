class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for i in nums:
            freq[i] += 1
        sorted_freq_list = sorted(freq, key = lambda x: freq[x], reverse = True)
        return sorted_freq_list[:k]