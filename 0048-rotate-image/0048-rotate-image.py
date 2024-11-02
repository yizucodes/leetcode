class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        # Traspose matrix
        for row in range(n):
            for col in range(row, len(matrix)):
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp

        # Reverse each row
        for r in range(n):
            matrix[r].reverse()

        return matrix