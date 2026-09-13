class Solution:
    def mySqrt(self, x: int) -> int:
        # find the largest i that i^2 <= x
        # T T T F F
        l, r = 0, x
        while l < r:
            mid = (l+r+1) // 2
            if mid * mid <= x:
                l = mid
            else:
                r = mid - 1
        return l
