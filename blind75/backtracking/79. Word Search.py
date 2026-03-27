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
board and word consists of only lowercase and uppercase English letters.
 """

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
    
#example usage
solution = Solution()
result = solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")
print(result)
#output: True

"""walkthrough
1. We define a helper function dfs that takes the current row, column, and index of the word we are trying to match.
2. If the index i equals the length of the word, it means we have found a match, so we return True.
3. We check if the current position is out of bounds, if the character at the current position does not match the current character in the word, or if the cell has already been visited (marked as '#'). If any of these conditions are true, we return False. 
4. We mark the current cell as visited by setting it to '#'.
5. We recursively call dfs for the four adjacent cells (down, up, right, left) and check if any of those calls return True. 
6. After exploring all adjacent cells, we restore the original value of the current cell (backtracking) and return the result of the recursive calls.   
7. We iterate through each cell in the board and call dfs starting from that cell. If any call returns True, we return True. If we finish iterating through all cells without finding a match, we return False. 
This approach effectively explores all possible paths in the grid while ensuring that we do not reuse cells, and it efficiently backtracks when a path does not lead to a solution. The time complexity is O(N * 3^L), where N is the number of cells in the board and L is the length of the word, since each cell can lead to at most 3 unvisited neighbors (after the first step). The space complexity is O(L) for the recursion stack."""