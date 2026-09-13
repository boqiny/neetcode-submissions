class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        # [4,5,0,1,2,3] -> [4,5,0,1] -> [4,5,0] -> [0]
        while l < r:
            mid = (l+r) // 2
            if nums[mid] > nums[r]: # ans is on the right
                l = mid + 1
            else: # ans is on the left, mid might be ans
                r = mid
        return nums[r]

            
