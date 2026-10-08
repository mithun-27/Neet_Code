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
-231 <= matrix[i][j] <= 231 - 1"""

#answer:
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


#example usage:
matrix1 = [[1,1,1],[1,0,1],[1,1,1]]
solution = Solution()
solution.setZeroes(matrix1)
print(matrix1)  # Output: [[1,0,1],[0,0,0],[1,0,1]] 

matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
solution.setZeroes(matrix2)
print(matrix2)  # Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


"""Walkthrough:

1. We are given a matrix and need to set an entire row and column to `0` whenever any element in that row or column is `0`.
2. The main challenge is to do this in-place without using extra `O(ROWS + COLS)` space.
3. This solution uses the first row and first column of the matrix itself as marker storage.
4. We also use a separate boolean variable `rowZero` to remember whether the first row originally contained a zero.
5. We first scan every cell in the matrix.
6. Whenever we find `matrix[r][c] == 0`, we mark the corresponding column by setting:
   `matrix[0][c] = 0`.
7. If the zero is not in the first row (`r > 0`), we also mark the corresponding row by setting:
   `matrix[r][0] = 0`.
8. If the zero is in the first row, we cannot use `matrix[0][0]` alone to distinguish whether the first row should become zero, so we set:
   `rowZero = True`.
9. After this first pass, the first row tells us which columns must be zeroed, and the first column tells us which rows must be zeroed.
10. We then process the inner part of the matrix, starting from row `1` and column `1`.
11. For every cell `(r, c)`, if either `matrix[0][c] == 0` or `matrix[r][0] == 0`, then that cell belongs to a marked row or column.
12. Therefore, we set:
    `matrix[r][c] = 0`.
13. We intentionally skip the first row and first column during this step because they are currently being used as markers.
14. After updating the inner matrix, we handle the first column separately.
15. If `matrix[0][0] == 0`, it means the first column must become zero.
16. In that case, we iterate through all rows and set:
    `matrix[r][0] = 0`.
17. Finally, we handle the first row separately using the `rowZero` flag.
18. If `rowZero` is `True`, it means the first row originally contained at least one zero.
19. Therefore, we iterate through every column and set:
    `matrix[0][c] = 0`.
20. At this point, every row and column that originally contained a zero has been completely converted to zero.
21. The key idea is to reuse the first row and first column as marker arrays instead of creating separate arrays.
22. The extra `rowZero` variable is necessary because `matrix[0][0]` is shared by both the first row and first column and cannot represent both states independently.
23. This approach modifies the matrix directly, so no additional matrix or marker arrays are required.
24. The time complexity is `O(ROWS × COLS)` because the matrix is scanned a constant number of times.
25. The auxiliary space complexity is `O(1)` because only a few variables are used.
"""