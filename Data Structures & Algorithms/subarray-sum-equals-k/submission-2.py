class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # k = sum(nums[i:j]) = prefix[j] - prefix[i] = k
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        cur_sum = 0
        count = 0
        for num in nums:
            cur_sum += num
            old_sum = cur_sum - k
            if old_sum in prefix_count:
                count += prefix_count[old_sum]
            prefix_count[cur_sum] += 1
        return count
            

