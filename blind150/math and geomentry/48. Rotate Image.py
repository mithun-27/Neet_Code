# Rotate Image
"""You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000"""

#answer:
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]



#example 1:
matrix = [[1,2,3],[4,5,6],[7,8,9]]
solution = Solution()
solution.rotate(matrix)
print(matrix)  # Output: [[7,4,1],[8,5,2],[9,6,3]]


#example 2:
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
solution = Solution()
solution.rotate(matrix)
print(matrix)  # Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]


"""Walkthrough:

1. We are given an `n × n` matrix and need to rotate it 90 degrees clockwise in-place.
2. Instead of creating another matrix, this solution performs the rotation using two operations: reversing the rows and then transposing the matrix.
3. First, `matrix.reverse()` reverses the order of all rows.
4. This means the first row becomes the last row, the second row moves toward the bottom, and the last row becomes the first row.
5. For example, the matrix `[[1,2,3],[4,5,6],[7,8,9]]` becomes `[[7,8,9],[4,5,6],[1,2,3]]` after reversing.
6. After reversing the rows, we transpose the matrix.
7. Transposing means converting rows into columns by swapping `matrix[i][j]` with `matrix[j][i]`.
8. We iterate through each row using `i`.
9. For every row, the inner loop starts from `i + 1` instead of `0`.
10. This is because elements on the main diagonal do not need to be changed.
11. It also prevents the same pair of elements from being swapped twice.
12. For every pair `(i, j)`, we perform:
    `matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]`.
13. This swaps the element above the main diagonal with the corresponding element below the main diagonal.
14. After all required swaps are completed, the reversed matrix has been fully transposed.
15. Continuing the example, `[[7,8,9],[4,5,6],[1,2,3]]` becomes `[[7,4,1],[8,5,2],[9,6,3]]`.
16. This final matrix is exactly the original matrix rotated 90 degrees clockwise.
17. The key idea is that reversing the rows performs a vertical flip, and transposing that flipped matrix produces a clockwise rotation.
18. Because all operations are performed directly on the original matrix, no additional matrix is required.
19. The time complexity is `O(n²)` because the algorithm processes roughly half of the `n²` matrix elements during the transpose.
20. The auxiliary space complexity is `O(1)` because the rotation is performed in-place using only temporary variables for swapping.
"""