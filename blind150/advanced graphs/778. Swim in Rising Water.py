#778. Swim in Rising Water
"""You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

It starts raining, and water gradually rises over time. At time t, the water level is t, meaning any cell with elevation less than equal to t is submerged or reachable.

You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

Return the minimum time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).

 

Example 1:


Input: grid = [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.
Example 2:


Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation: The final route is shown.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 50
0 <= grid[i][j] < n2
Each value grid[i][j] is unique."""

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
        if self.Size[pu] < self.Size[pv]:
            pu, pv = pv, pu
        self.Size[pu] += self.Size[pv]
        self.Parent[pv] = pu
        return True

    def connected(self, u, v):
        return self.find(u) == self.find(v)

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        dsu = DSU(N * N)
        positions = sorted((grid[r][c], r, c) for r in range(N) for c in range(N))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for t, r, c in positions:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] <= t:
                    dsu.union(r * N + c, nr * N + nc)
            if dsu.connected(0, N * N - 1):
                return t

"""Walkthrough:
1. We want to find the minimum time `t` at which it becomes possible to travel from the top-left cell `(0,0)` to the bottom-right cell `(n-1,n-1)`. The water level rises with time, and a cell can only be entered when its elevation is less than or equal to the current time.
2. We can view the grid as a graph where each cell is a node and edges connect adjacent cells. The cost of moving to a cell is determined by its elevation because we must wait until the water reaches at least that height.
3. We use Dijkstra's Algorithm (or a minimum-priority BFS) to always explore the path that minimizes the maximum elevation encountered so far.
4. We initialize a min-heap with the starting cell `(0,0)`. The initial time required is `grid[0][0]` because we must wait until the starting cell is submerged.
5. Each heap entry stores `(current_time, row, col)`, where `current_time` represents the highest elevation encountered along the path to that cell.
6. We repeatedly remove the cell with the smallest `current_time` from the heap. This guarantees that we process cells in order of the minimum possible water level needed to reach them.
7. For each neighboring cell, we calculate the new required time as `max(current_time, neighbor_elevation)`. This is because we must wait until the water level is high enough for every cell on the path.
8. If the neighboring cell has not been visited, we add it to the heap with its newly calculated required time. The algorithm continues expanding the most promising path first.
9. When we reach the bottom-right cell `(n-1, n-1)`, the associated `current_time` is the minimum time required to connect the start and destination. The time complexity is `O(n² log n²)` = `O(n² log n)` because each cell may be inserted into the priority queue, and the auxiliary space complexity is `O(n²)` for the visited set and heap."""