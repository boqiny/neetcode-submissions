class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] := max money can rob until nums[i]
        # dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        n = len(nums)
        if n <= 2:
            return max(nums)
        dp = [0] * n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        print(dp)
        return dp[-1]