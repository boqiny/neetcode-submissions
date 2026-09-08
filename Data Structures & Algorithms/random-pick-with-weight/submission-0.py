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
        for i in range(len(self.prefix)):
            if self.prefix[i] >= target:
                return i
        # l, r = 0, len(self.prefix) - 1


        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()