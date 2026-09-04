class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        def rob_dp(nums: List[int]) -> int:
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-2] + nums[i], dp[i-1])
            return dp[-1]
        return max(rob_dp(nums[1:]), rob_dp(nums[:-1]))
