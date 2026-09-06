class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] := length of LIS ending at nums[i]
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j]+1, dp[i])
        return max(dp)