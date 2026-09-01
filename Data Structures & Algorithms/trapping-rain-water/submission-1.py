class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_l, max_r = [0] * n, [0] * n
        res = 0
        for i in range(1, n):
            max_l[i] = max(max_l[i-1],height[i-1])
        for i in range(n-2, -1, -1):
            max_r[i] = max(max_r[i+1],height[i+1])
        print(max_l)
        print(max_r)
        for i in range(1,n-1):
            print(i, min(max_l[i],max_r[i]) - height[i])
            if min(max_l[i],max_r[i]) - height[i] > 0:
                res += min(max_l[i],max_r[i]) - height[i]
        return res
