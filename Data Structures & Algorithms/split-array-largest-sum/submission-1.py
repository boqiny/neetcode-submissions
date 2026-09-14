class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def feasible(x) -> bool:
            count, cur = 1, 0
            for num in nums:
                if cur + num > x:
                    count += 1
                    cur = num
                else:
                    cur += num
            return count <= k

        l, r = max(nums), sum(nums)
        while l < r:
            mid = (l+r) // 2
            if feasible(mid):
                r = mid
            else:
                l = mid + 1
        return l

            
