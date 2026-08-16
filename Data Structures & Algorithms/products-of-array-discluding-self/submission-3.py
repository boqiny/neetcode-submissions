class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = [1] * n, [1] * n
        res = [1] * n
        for i in range(1, n):
            left[i] = nums[i-1] * left[i-1]
        # left [1,1,2,8]
        # right [48,24,6,1]
        for i in range(n-2, -1, -1):
            right[i] = nums[i+1] * right[i+1]
        for i in range(n):
            res[i] = left[i] * right[i]
        return res
    # Time,Space: O(n)
