#286. Walls And Gates
"""You are given a 
m
×
n
m×n 2D grid initialized with these three possible values:

-1 - A water cell that can not be traversed.
0 - A treasure chest.
INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest then the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

Modify the grid in-place.

Example 1:

Input: [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]

Output: [
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]
Example 2:

Input: [
  [0,-1],
  [2147483647,2147483647]
]

Output: [
  [0,-1],
  [1,2]
]
Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
grid[i][j] is one of {-1, 0, 2147483647}"""

#answer:
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addCell(r, c):
            if (min(r, c) < 0 or r == ROWS or c == COLS or
                (r, c) in visit or grid[r][c] == -1
            ):
                return
            visit.add((r, c))
            q.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1


"""Walkthrough:
1. We want to fill every empty room in the grid with the distance to its nearest treasure (gate). Walls (`-1`) cannot be crossed, and if a room cannot reach any treasure, it remains unchanged.
2. Instead of running a separate search from every empty room, we use a multi-source Breadth-First Search (BFS) by starting simultaneously from all treasure cells (`0`). This efficiently computes the shortest distance for every reachable room.
3. We first initialize a queue and a visited set. We traverse the entire grid, and whenever we find a treasure (`0`), we add its position to the queue and mark it as visited.
4. We define a helper function `addCell()` that adds a neighboring cell to the queue only if it is inside the grid, has not been visited, and is not a wall (`-1`).
5. We initialize the distance (`dist`) as `0`. Each level of the BFS represents rooms that are exactly `dist` steps away from the nearest treasure.
6. While the queue is not empty, we process all cells currently in the queue (one BFS level). For each cell, we update its value in the grid with the current distance.
7. After updating a cell, we attempt to add its four neighboring cells (up, down, left, and right) to the queue using the `addCell()` helper function. These neighbors will be processed in the next BFS level.
8. After processing all cells in the current level, we increment `dist` by `1`. This ensures that cells in the next level receive the correct shortest distance from the nearest treasure.
9. The algorithm continues until the queue becomes empty. Since BFS explores cells level by level from all treasures simultaneously, every room is assigned its minimum distance to the nearest treasure. The time complexity is `O(ROWS × COLS)` because each cell is visited at most once, and the auxiliary space complexity is `O(ROWS × COLS)` for the queue and visited set."""