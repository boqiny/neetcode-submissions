class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        counts = {0: 1}
        for x in nums:
            new = defaultdict(int)
            for s, c in counts.items():
                new[s+x] += c
                new[s-x] += c
            counts = new
        return counts[target]

