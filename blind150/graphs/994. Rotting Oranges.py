#994. Rotting Oranges
"""You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2"""

#answer:
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        time = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while fresh > 0:
            flag = False
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 2:
                        for dr, dc in directions:
                            row, col = r + dr, c + dc
                            if (row in range(ROWS) and
                                col in range(COLS) and
                                grid[row][col] == 1):
                                grid[row][col] = 3
                                fresh -= 1
                                flag = True

            if not flag:
                return -1

            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 3:
                        grid[r][c] = 2

            time += 1

        return time

#example 1:
"""Input
grid =
[[2,1,1],[1,1,0],[0,1,1]]
Output
4
Expected
4"""
#example 2:
"""Input
grid =
[[2,1,1],[0,1,1],[1,0,1]]
Output
-1
Expected
-1"""

"""Walkthrough:
1. We want to determine the minimum number of minutes required for all fresh oranges (`1`) to become rotten (`2`). A rotten orange infects its adjacent fresh oranges (up, down, left, and right) every minute.
2. We first count the total number of fresh oranges in the grid. If there are no fresh oranges, the answer will be `0` because no time is needed.
3. We define the four possible movement directions: right, left, down, and up. These represent the adjacent cells that a rotten orange can infect.
4. While there are still fresh oranges remaining, we simulate one minute of rotting at a time. A flag variable is used to track whether any fresh orange becomes rotten during the current minute.
5. We scan the entire grid and look for currently rotten oranges (`2`). For each rotten orange, we check its four neighboring cells.
6. If a neighboring cell contains a fresh orange (`1`), we temporarily mark it as `3`. This indicates that it will become rotten at the end of the current minute, preventing it from infecting other oranges during the same minute.
7. Every time a fresh orange is marked as `3`, we decrease the fresh orange count and set the flag to `True` because at least one orange has rotted during this minute.
8. After scanning the entire grid, if no fresh orange became rotten (`flag == False`) while fresh oranges still exist, it means some fresh oranges are unreachable. In this case, we return `-1`.
9. We then convert all temporary `3`s into rotten oranges (`2`) and increment the time by one minute. This completes the simulation of the current minute.
10. The process repeats until all fresh oranges have become rotten. The final value of `time` is returned as the answer. The time complexity is `O((ROWS × COLS)^2)` because the grid may be scanned multiple times, and the auxiliary space complexity is `O(1)` since no extra data structures proportional to the grid size are used."""