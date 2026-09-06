class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2 != 0:
            return False
        target = nums_sum // 2
        reachable = {0}
        for x in nums:
            reachable |= {s + x for s in reachable}
        return target in reachable