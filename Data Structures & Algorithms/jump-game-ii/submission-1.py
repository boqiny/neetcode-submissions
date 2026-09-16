class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        current_end = 0
        jumps = 0

        for i in range(len(nums) - 1):        # 注意不遍历最后一个
            farthest = max(farthest, i + nums[i])
            if i == current_end:              # 当前层扫完了
                jumps += 1                    # 迈进下一层
                current_end = farthest        # 新边界
        return jumps