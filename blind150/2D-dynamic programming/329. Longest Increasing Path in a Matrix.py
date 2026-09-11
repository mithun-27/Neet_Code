#329. Longest Increasing Path in a Matrix
"""Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

 

Example 1:


Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:


Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
Example 3:

Input: matrix = [[1]]
Output: 1
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1"""


#answer:
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        indegree = [[0] * COLS for _ in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                for d in directions:
                    nr, nc = d[0] + r, d[1] + c
                    if (0 <= nr < ROWS and 0 <= nc < COLS and
                        matrix[nr][nc] < matrix[r][c]
                    ):
                        indegree[r][c] += 1

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if indegree[r][c] == 0:
                    q.append([r, c])

        LIS = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for d in directions:
                    nr, nc = r + d[0], c + d[1]
                    if (0 <= nr < ROWS and 0 <= nc < COLS and
                        matrix[nr][nc] > matrix[r][c]
                    ):
                        indegree[nr][nc] -= 1
                        if indegree[nr][nc] == 0:
                            q.append([nr, nc])
            LIS += 1
        return LIS

"""Walkthrough:
1. We want to find the length of the Longest Increasing Path (LIP) in the matrix, where we can move only up, down, left, or right.
2. Instead of using DFS + Memoization, this solution models the matrix as a Directed Acyclic Graph (DAG).
3. For every cell `(r, c)`, we create directed edges from smaller-valued neighbors to larger-valued neighbors. This means a valid increasing path follows the direction of the edges.
4. We compute an `indegree` for every cell:
   - `indegree[r][c]` = number of neighboring cells with smaller values that can reach `(r, c)`.
5. A cell with `indegree = 0` has no smaller neighbor. Therefore, it can be the starting point of an increasing path.
6. We add all cells with `indegree = 0` into a queue. These form the first layer of a topological ordering.
7. We then perform a multi-source BFS (Kahn's Topological Sort):
   - Remove all cells in the current layer.
   - Visit their larger neighbors.
   - Decrease the neighbor's indegree.
   - If a neighbor's indegree becomes `0`, add it to the queue for the next layer.
8. Each BFS layer represents one level in an increasing path. Therefore, after processing an entire layer, we increment `LIS` by `1`.
9. When the queue becomes empty, all cells have been processed. The number of BFS layers traversed is exactly the length of the longest increasing path. The time complexity is `O(ROWS × COLS)` because each cell and edge is processed a constant number of times, and the auxiliary space complexity is `O(ROWS × COLS)` for the indegree matrix and queue."""