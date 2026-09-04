#62. Unique Paths
"""There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 

Constraints:

1 <= m, n <= 100"""

#answer:
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        if m < n:
            m, n = n, m

        res = j = 1
        for i in range(m, m + n - 1):
            res *= i
            res //= j
            j += 1

        return res


#example:
"""Input
m =
3
n =
7
Output
28
Expected
28"""


"""Walkthrough:
1. We want to find the number of unique paths from the top-left corner to the bottom-right corner of an `m × n` grid.
2. At each step, we can only move either right or down. To reach the destination, we must make exactly:
   - `m - 1` downward moves
   - `n - 1` rightward moves
3. Therefore, every valid path consists of a total of:
   `m + n - 2`
   moves.
4. The problem now becomes: among these total moves, choose which positions will be downward moves (or equivalently, which positions will be rightward moves).
5. This is a combinations problem. The number of unique paths is:
   `C(m+n-2, n-1)`
   or equivalently
   `C(m+n-2, m-1)`.
6. To reduce the number of iterations, the code ensures that `m >= n` by swapping them if necessary. This allows us to compute the smaller combination efficiently.
7. The variable `res` stores the running value of the combination. Instead of calculating large factorials, we build the result incrementally using:
   `res = res * numerator / denominator`
8. The loop computes:
   `C(m+n-2, n-1)`
   step by step, multiplying by the next numerator term and dividing by the next denominator term at each iteration. Integer division (`//`) is safe because combinations always produce whole numbers.
9. After all terms have been processed, `res` contains the total number of unique paths. The time complexity is `O(min(m, n))` because only the smaller dimension determines the number of iterations, and the auxiliary space complexity is `O(1)` since only a few variables are used."""