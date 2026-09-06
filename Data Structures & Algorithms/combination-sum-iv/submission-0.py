class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # dp[i] := # of combinations to add up to i
        # dp[i] = dp[i - nums[0]] + dp[i - nums[1]] + ... （i-x >= 0）
        n = len(nums)
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for x in nums:
                if i - x >= 0:
                    dp[i] += dp[i-x]
        return dp[-1]
            