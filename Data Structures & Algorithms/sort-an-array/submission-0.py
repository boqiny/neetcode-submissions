class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge_sort(lo, hi):
            if hi - lo <= 1:
                return
            mid = (lo + hi) // 2
            merge_sort(lo, mid)
            merge_sort(mid, hi)
            left, right = nums[lo:mid], nums[mid:hi]
            i = j = 0
            for k in range(lo, hi):
                if j >= len(right) or (i < len(left) and left[i] <= right[j]):
                    nums[k] = left[i]
                    i += 1
                else:
                    nums[k] = right[j]
                    j += 1
        
        merge_sort(0, len(nums))
        return nums