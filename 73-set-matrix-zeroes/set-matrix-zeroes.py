class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        row_arr = [False] * n
        col_arr = [False] * m
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    row_arr[i] = True
                    col_arr[j] = True
        
        for i in range(n):
            for j in range(m):
                if row_arr[i] or col_arr[j]:
                    matrix[i][j] = 0

