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

"""walkthrough:
1. We initialize an empty list `res` to store the elements in spiral order.
2. We define a list of `directions` that represent the four possible movements: right  (0, 1), down (1, 0), left (0, -1), and up (-1, 0).
3. We also define a list `steps` that keeps track of the number of steps we can take in the current direction. Initially, we can move `len(matrix[0])` steps to the right and `len(matrix) - 1` steps down.
4. We start at the position (0, -1) and initialize the direction index `d` to 0 (indicating the right direction).
5. We enter a while loop that continues as long as there are steps to take in the current direction (checked using `steps[d & 1]`).
6. Inside the loop, we iterate for the number of steps in the current direction, updating our position (r, c) based on the current direction and appending the corresponding matrix element to `res`.
7. After completing the steps in the current direction, we decrement the step count for that direction and update the direction index `d` to move to the next direction (right -> down -> left -> up).
8. Finally, we return the list `res` containing the elements in spiral order.
This approach has a time complexity of O(m*n) since we visit each element of the matrix once, and a space complexity of O(m*n) for storing the result in the list `res`.
"""