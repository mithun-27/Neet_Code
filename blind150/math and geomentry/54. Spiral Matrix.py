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

#answer:
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
solution = Solution()
print(solution.spiralOrder(matrix))  # Output: [1,2,3,6,9,8,7,4,5]


#example 2:
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
solution = Solution()
print(solution.spiralOrder(matrix))  # Output: [1,2,3,4,8,12,11,10,9,5,6,7]


"""Walkthrough:

1. We are given an `m × n` matrix and need to return all elements in spiral order.
2. Spiral order means traversing the matrix layer by layer in the sequence: right → down → left → up.
3. Instead of maintaining four boundaries (`top`, `bottom`, `left`, `right`), this solution uses direction vectors and step counts.
4. We create a result list `res` to store elements in the order they are visited.
5. The array

   ```python
   directions = [(0,1), (1,0), (0,-1), (-1,0)]
   ```

   represents movement in the directions:

   * Right
   * Down
   * Left
   * Up
6. The array

   ```python
   steps = [len(matrix[0]), len(matrix) - 1]
   ```

   stores the number of horizontal and vertical moves remaining.
7. Initially:

   * Horizontal movement requires `cols` steps.
   * Vertical movement requires `rows - 1` steps.
8. We start from:

   ```python
   r = 0
   c = -1
   d = 0
   ```
9. The column is initialized to `-1` so that the first move to the right lands exactly on `(0,0)`.
10. The variable `d` represents the current direction index.
11. The loop continues while:

```python
steps[d & 1]
```

is greater than zero.
12. The expression `d & 1` determines whether we are currently moving horizontally or vertically.
13. When `d` is `0` or `2`, `d & 1 = 0`, so horizontal steps are used.
14. When `d` is `1` or `3`, `d & 1 = 1`, so vertical steps are used.
15. For the current direction, we move exactly the required number of steps.
16. During each step:

```python
r += directions[d][0]
c += directions[d][1]
```

updates the current position.
17. The matrix value at that position is appended to `res`.
18. After completing movement in one direction, we reduce:

```python
steps[d & 1] -= 1
```

19. This is because one outer layer of the matrix has now been completely traversed.
20. We then rotate to the next direction:

```python
d = (d + 1) % 4
```

21. The directions therefore cycle as:
    Right → Down → Left → Up → Right ...
22. After every two turns, the required number of steps decreases because the spiral moves inward to a smaller layer.
23. Eventually both horizontal and vertical step counts become zero.
24. At that point, every matrix element has been visited exactly once.
25. The result list `res` contains all elements in spiral order and is returned.
26. The key insight is that horizontal and vertical step counts shrink after each completed traversal, naturally simulating the spiral layers.
27. The time complexity is `O(m × n)` because every element is visited exactly once.
28. The auxiliary space complexity is `O(1)` excluding the output array.
"""