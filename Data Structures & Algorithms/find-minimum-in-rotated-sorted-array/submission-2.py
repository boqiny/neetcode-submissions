class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [4,5,6,7',0,1,2] -> [0,1',2] -> [0',1] -> [0]
        # [3,4,5',1,2] -> [1',2] -> [1]
        # [2',1] -> [1]
        # [1,2,3',4,5] -> [1,2',3] -> [1',2] -> [1]
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l+r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[r]
                
                
