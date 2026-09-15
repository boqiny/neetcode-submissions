class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        counts = {0: 1}
        for num in nums:
            new = defaultdict(int)
            for n, c in counts.items():
                new[n+num] += c
                new[n-num] += c
            counts = new
        return counts[target]