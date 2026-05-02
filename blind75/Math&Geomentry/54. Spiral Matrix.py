#54. Spiral Matrix
"""Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100"""

#answer
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        steps = [len(matrix[0]), len(matrix) - 1]

        r, c, d = 0, -1, 0
        while steps[d & 1]:
            for i in range(steps[d & 1]):
                r += directions[d][0]
                c += directions[d][1]
                res.append(matrix[r][c])
            steps[d & 1] -= 1
            d += 1
            d %= 4
        return res

#example 1:
matrix = [[1,2,3],[4,5,6],[7,8,9]]
s = Solution()
print(s.spiralOrder(matrix)) # Output: [1,2,3,6,9,8,7,4,5]
#example 2:
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
s = Solution()
print(s.spiralOrder(matrix)) # Output: [1,2,3,4,8,12,11,10,9,5,6,7]
