class Solution:
    def mySqrt(self, x: int) -> int:
        # find the largest i that i^2 <= x
        # = （第一个 >= x 的 i） - 1
        l , r = 0, x+1
        while l < r:
            mid = (l+r) // 2
            if mid ** 2 <= x:
                l = mid + 1
            else:
                r = mid
        return r-1