#79. Word Search
"""Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters."""

#answer
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                word[i] != board[r][c] or board[r][c] == '#'):
                return False

            board[r][c] = '#'
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            board[r][c] = word[i]
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False

#example 1
"""Input: 
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
],
word = "CAT"

Output: true"""
#example 2 
"""Input: 
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
],
word = "BAT"

Output: false"""

"""Walkthrough:
1. We want to determine whether the given `word` can be formed by sequentially connecting adjacent cells (up, down, left, or right) in the board, where each cell can be used only once in a single path.
2. We iterate through every cell in the board and treat each cell as a possible starting position for the word.
3. From each starting cell, we perform a depth-first search (DFS) to check whether the remaining characters of the word can be matched by moving to adjacent cells.
4. During the DFS, we first check the base case. If the current index reaches the length of the word, it means every character has been matched successfully, so we return `True`.
5. We then check whether the current position is out of bounds, whether the character in the board does not match the current character of the word, or whether the cell has already been visited. If any of these conditions are true, we return `False`.
6. If the current cell is valid, we temporarily mark it as visited by replacing its value with a special character (such as `'#'`). This prevents revisiting the same cell while constructing the current path.
7. We recursively explore the four possible directions (down, up, right, and left) to match the next character of the word. If any recursive call returns `True`, the current search path is successful.
8. After exploring all directions, we restore the original character in the board (backtracking) so that the cell can be used in other search paths starting from different positions.
9. If a valid path is found from any starting cell, we immediately return `True`. If all possible starting positions have been explored without matching the entire word, we return `False`. The time complexity is `O(ROWS × COLS × 4^L)`, where `L` is the length of the word, and the auxiliary space complexity is `O(L)` for the recursion stack."""