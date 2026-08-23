class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # k = sum(nums[i:j]) = prefix[j] - prefix[i] = k
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        cur_sum = 0
        count = 0
        for i in range(1, len(nums)+1):
            cur_sum += nums[i-1]
            old_sum = cur_sum - k
            if old_sum in prefix_count:
                count += prefix_count[old_sum]
            prefix_count[cur_sum] += 1
        return count
            

