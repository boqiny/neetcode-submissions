class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ctr = Counter(nums)
        return sorted(ctr, key = lambda x: ctr[x], reverse = True)[:k]