import random
from typing import List

class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        total = 0
        for weight in w:
            total += weight
            self.prefix.append(total)
        self.total = total

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)  # 两端都包含
        # find the first prefix >= target:
        l, r = 0, len(self.prefix) - 1
        while l < r:
            mid = (l+r) // 2
            if self.prefix[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l



        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()