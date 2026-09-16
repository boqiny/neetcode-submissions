class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_count = 0
        for x in nums_set:
            if x-1 not in nums_set:
                count = 1
                cur = x
                while cur + 1 in nums_set:
                    count += 1
                    cur = cur + 1
                max_count = max(max_count, count)
        return max_count