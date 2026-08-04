#200. Number of Islands
"""Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'."""

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

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dsu = DSU(ROWS * COLS)

        def index(r, c):
            return r * COLS + c

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        islands = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    islands += 1
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if (nr < 0 or nc < 0 or nr >= ROWS or
                            nc >= COLS or grid[nr][nc] == "0"
                        ):
                            continue

                        if dsu.union(index(r, c), index(nr, nc)):
                            islands -= 1

        return islands

#example 1 :
"""Input
grid =
[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
Output
1
Expected
1"""

#example 2 :
"""Input
grid =
[["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
Output
3
Expected
3"""

"""Walkthrough:
1. We want to count the number of islands in the given binary grid, where an island is formed by connecting adjacent land cells (`'1'`) horizontally or vertically.
2. We iterate through every cell in the grid. Whenever we encounter a land cell (`'1'`) that has not been visited, we have discovered a new island, so we increment the island count.
3. From the newly discovered land cell, we perform a depth-first search (DFS) or breadth-first search (BFS) to visit all connected land cells belonging to the same island.
4. During the traversal, we first check whether the current position is out of bounds or whether the current cell is water (`'0'`). If either condition is true, we stop exploring that path.
5. If the current cell is land, we mark it as visited (for example, by changing `'1'` to `'0'` or by storing it in a visited set). This ensures that the same land cell is not counted multiple times.
6. We then recursively (or iteratively) explore the four adjacent directions: up, down, left, and right. Every connected land cell is marked as visited, meaning the entire island is explored in a single traversal.
7. After the DFS/BFS completes, all cells belonging to the current island have been visited. The next unvisited land cell encountered in the grid will represent a new island.
8. The algorithm continues until every cell in the grid has been processed. Since each land cell is visited exactly once, every island is counted exactly once.
9. Let `m` and `n` be the number of rows and columns in the grid. The time complexity is `O(m × n)` because each cell is visited at most once. The auxiliary space complexity is `O(m × n)` in the worst case for the recursion stack (or queue/visited set), depending on the traversal method."""