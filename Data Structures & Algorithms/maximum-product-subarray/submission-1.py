class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # cur_max[i] := max product of end with nums[i]
        # cur_min[i] := min product of end with nums[i]
        n = len(nums)
        cur_max = [0] * n
        cur_min = [0] * n
        cur_max[0] = cur_min[0] = nums[0]
        for i in range(1, n):
            cur_max[i] = max(nums[i], cur_max[i-1] * nums[i], cur_min[i-1] * nums[i])
            cur_min[i] = min(nums[i], cur_max[i-1] * nums[i], cur_min[i-1] * nums[i])
        return max(cur_max)