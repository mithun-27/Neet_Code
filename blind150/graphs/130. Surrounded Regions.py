#130. Surrounded Regions
"""You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: A region is surrounded if none of the 'O' cells in that region are on the edge of the board. Such regions are completely enclosed by 'X' cells.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

 

Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation:


In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

Example 2:

Input: board = [["X"]]

Output: [["X"]]

 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'."""

#answer:
class DSU:
    def __init__(self, n):
        self.Parent = list(range(n + 1))
        self.Size = [1] * (n + 1)

    def find(self, node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.Size[pu] >= self.Size[pv]:
            self.Size[pu] += self.Size[pv]
            self.Parent[pv] = pu
        else:
            self.Size[pv] += self.Size[pu]
            self.Parent[pu] = pv
        return True

    def connected(self, u, v):
        return self.find(u) == self.find(v)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dsu = DSU(ROWS * COLS + 1)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] != "O":
                    continue
                if (r == 0 or c == 0 or
                    r == (ROWS - 1) or c == (COLS - 1)
                ):
                    dsu.union(ROWS * COLS, r * COLS + c)
                else:
                    for dx, dy in directions:
                        nr, nc = r + dx, c + dy
                        if board[nr][nc] == "O":
                            dsu.union(r * COLS + c, nr * COLS + nc)

        for r in range(ROWS):
            for c in range(COLS):
                if not dsu.connected(ROWS * COLS, r * COLS + c):
                    board[r][c] = "X"


#example 1:
"""Input
board =
[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output
[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Expected
[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
"""

#example 2:
"""Input
board =
[["X"]]
Output
[["X"]]
Expected
[["X"]]"""


"""Walkthrough:
1. We want to capture all regions of `'O'` that are completely surrounded by `'X'`. Any `'O'` connected to the boundary of the board cannot be captured because it is not fully enclosed.
2. Instead of checking every region individually, we first identify all `'O'` cells that are connected to the board's boundary. These cells are guaranteed to remain `'O'`.
3. We traverse the boundary cells (first row, last row, first column, and last column). Whenever we find an `'O'`, we start a DFS or BFS from that cell.
4. During the DFS/BFS, we mark every reachable `'O'` as a temporary character (for example, `'T'`) to indicate that it is connected to the boundary and should not be captured.
5. The search continues through all horizontally and vertically adjacent `'O'` cells, marking the entire boundary-connected region as safe.
6. After processing all boundary cells, every remaining `'O'` on the board must belong to a surrounded region because it is not connected to any edge.
7. We then traverse the entire board. If a cell contains `'O'`, we change it to `'X'` because it is fully surrounded and should be captured.
8. If a cell contains the temporary marker `'T'`, we restore it back to `'O'` because it was connected to the boundary and must remain unchanged.
9. The algorithm modifies the board in-place and ensures that only surrounded regions are captured. The time complexity is `O(m × n)` because each cell is visited at most once, and the auxiliary space complexity is `O(m × n)` in the worst case due to the DFS/BFS recursion stack or queue."""