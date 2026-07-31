#51. N-Queens
"""The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]
 

Constraints:

1 <= n <= 9"""

#answer
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = 0
        posDiag = 0
        negDiag = 0
        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            nonlocal col, posDiag, negDiag
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if ((col & (1 << c)) or (posDiag & (1 << (r + c)))
                    or (negDiag & (1 << (r - c + n)))):
                    continue
                col ^= (1 << c)
                posDiag ^= (1 << (r + c))
                negDiag ^= (1 << (r - c + n))
                board[r][c] = "Q"

                backtrack(r + 1)

                col ^= (1 << c)
                posDiag ^= (1 << (r + c))
                negDiag ^= (1 << (r - c + n))
                board[r][c] = "."

        backtrack(0)
        return res


"""Example 1:



Input: n = 4

Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There are two different solutions to the 4-queens puzzle.

Example 2:

Input: n = 1

Output: [["Q"]]"""

"""Walkthrough:
1. We want to place `n` queens on an `n × n` chessboard such that no two queens attack each other. This means no two queens can share the same row, column, or diagonal.
2. We use a backtracking (depth-first search) approach and place one queen at a time, moving row by row through the board.
3. To efficiently check whether a position is safe, we maintain three sets: one for occupied columns, one for the positive diagonals (`row + col`), and one for the negative diagonals (`row - col`).
4. For each row, we try placing a queen in every column. Before placing it, we check whether the column or either diagonal is already occupied. If it is, we skip that position.
5. If the position is safe, we place the queen on the board, mark its column and diagonals as occupied, and recursively move to the next row.
6. If we successfully place queens in all `n` rows, we have found a valid board configuration. We convert the board into the required string format and add it to the result list.
7. After returning from the recursive call, we backtrack by removing the queen from the current position and removing its column and diagonals from the occupied sets. This allows us to explore other possible placements.
8. The algorithm continues until every possible queen placement has been explored. Backtracking ensures that all distinct valid board configurations are generated exactly once.
9. The time complexity is approximately `O(n!)` in the worst case because we try different column placements for each row while pruning invalid positions early. The auxiliary space complexity is `O(n)` for the recursion stack and the sets used to track occupied columns and diagonals (excluding the output list)."""