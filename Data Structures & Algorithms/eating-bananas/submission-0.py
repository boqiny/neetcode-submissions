class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)
        # [1, max_pile]
        def canFinish(k):
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)   # 或者 (p + k - 1) // k
            return hours <= h
        l, r = 1, max_pile
        while l < r:
            k = (l + r) // 2
            if canFinish(k):
                r = k
            else:
                l = k + 1
        return l
        
        