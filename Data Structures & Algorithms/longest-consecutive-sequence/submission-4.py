class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for i in nums:
            if i - 1 not in nums: # trick: only start at beginning
                j = i
                while j + 1 in nums:
                    j += 1
                longest = max(longest, j-i+1)
        return longest
# Time:  O(n) average
# Space: O(n)