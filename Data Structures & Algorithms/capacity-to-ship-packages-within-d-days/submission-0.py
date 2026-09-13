class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        
        def feasible(k) -> bool:
            count = 1
            cur = 0
            for w in weights:
                if cur + w > k:
                    count += 1
                    cur = w
                else:
                    cur += w
            return count <= days


        while l < r:
            mid = (l+r) // 2
            if feasible(mid):
                r = mid
            else:
                l = mid + 1
        return l
