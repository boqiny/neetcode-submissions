class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        print(freq)
        bucket = [[] for _ in range(len(nums)+1)]
        for num, count in freq.items():
            bucket[count].append(num)
        print(bucket)
        res = []
        for i in range(len(nums), -1, -1):
            if bucket[i]:
                for num in bucket[i]:
                    res.append(num)
                    if len(res) == k:
                        return res
