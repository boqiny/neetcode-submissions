class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # row: mid // cols, col: mid % cols
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows * cols - 1
        while l <= r:
            mid = (l+r) // 2
            cur = matrix[mid // cols][mid % cols]
            if target == cur:
                return True
            elif target > cur:
                l = mid + 1
            else:
                r = mid - 1
        return False

