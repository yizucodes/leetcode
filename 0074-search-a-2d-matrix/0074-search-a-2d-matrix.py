class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # binary search to find correct row
        rows = len(matrix)
        cols = len(matrix[0])
        totalI = rows * cols
        l = 0
        r = totalI - 1

        # calculate flatten indexed in the while loop
        while l <= r:
            m = (l + r) // 2
            row = m // cols
            col = m % cols

            if matrix[row][col] == target:
                return True

            # go right target > num[m]
            if target > matrix[row][col]:
                l = m + 1
            else:
                r = m - 1
            

        return False




        