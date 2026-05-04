#73. Set Matrix Zeroes
"""Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
"""
#answer
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0

#example 1:
matrix = [[1,1,1],[1,0,1],[1,1,1]]
s = Solution()
s.setZeroes(matrix)
print(matrix) # Output: [[1,0,1],[0,0,0],[1,0,1]]

#example 2:
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
s = Solution()
s.setZeroes(matrix)
print(matrix) # Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]] 

"""walkthrough:
1. We first determine the number of rows and columns in the matrix and initialize a boolean variable `rowZero` to keep track of whether the first row contains any zeros.   
2. We iterate through the matrix to find any zeros. If we find a zero at position (r, c), we set the first element of that column (matrix[0][c]) to zero and, if r > 0, we set the first element of that row (matrix[r][0]) to zero. If the zero is in the first row, we set `rowZero` to True. This way, we use the first row and column as markers to indicate which rows and columns should be set to zero later on. 
3. After marking the rows and columns, we iterate through the matrix again starting from the second row and second column. If either the first element of the current column (matrix[0][c]) or the first element of the current row (matrix[r][0]) is zero, we set the current element (matrix[r][c]) to zero.  
4. Finally, we check if the first element of the matrix (matrix[0][0]) is zero. If it is, we set the entire first column to zero. We also check if `rowZero` is True, and if so, we set the entire first row to zero. This ensures that all rows and columns that were marked with zeros are properly set to zero in the final output.
5. The function modifies the input matrix in place, so there is no return value.
"""