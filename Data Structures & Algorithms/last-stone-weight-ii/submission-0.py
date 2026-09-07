class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # sum(set1)=a; sum(set2)=S-a; min (diff=|S - 2a|) => a -> S//2
        # dp[i] := if can sum up to i
        stones_sum = sum(stones)
        target = stones_sum // 2
        n = len(stones)
        reachable = {0}
        for x in stones:
            reachable |= {s+x for s in reachable if s + x <= target}
        best = max(reachable)
        
        return stones_sum - 2 * best

                    

            