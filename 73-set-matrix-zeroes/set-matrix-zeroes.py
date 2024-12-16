class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])

        def mark_row(i):
            for j in range(m):
                if matrix[i][j] != 0:
                    matrix[i][j] = 'weee'
        def mark_col(j):
            for i in range(n):
                if matrix[i][j]!=0:
                    matrix[i][j]='weee'
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    mark_row(i)
                    mark_col(j)

        for i in range(n):
            for j in range(m):
                if matrix[i][j]=='weee':
                    matrix[i][j]=0
        
        