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