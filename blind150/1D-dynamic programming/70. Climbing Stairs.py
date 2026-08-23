#70. Climbing Stairs
"""You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45"""

#answer :
class Solution:
    def climbStairs(self, n: int) -> int:
        sqrt5 = math.sqrt(5)
        phi = (1 + sqrt5) / 2
        psi = (1 - sqrt5) / 2
        n += 1
        return round((phi**n - psi**n) / sqrt5)

#example:
"""Input
n =
2
Output
2
Expected
2"""

#walkthrough:
"""
1. We want to find the number of distinct ways to climb `n` stairs when we can take either 1 step or 2 steps at a time.
2. Notice that the number of ways to reach a stair follows the Fibonacci sequence because to reach stair `n`, we must come either from stair `n-1` (taking 1 step) or stair `n-2` (taking 2 steps).
3. Therefore, the recurrence relation is:
   `ways(n) = ways(n-1) + ways(n-2)`.
4. Instead of computing Fibonacci numbers using recursion or dynamic programming, this solution uses Binet's Formula, a mathematical formula that directly calculates the nth Fibonacci number.
5. First, we compute `sqrt(5)`, which is required for the formula.
6. We then calculate the two constants:
   - `phi = (1 + sqrt(5)) / 2` (the Golden Ratio)
   - `psi = (1 - sqrt(5)) / 2`
7. Since the number of ways to climb `n` stairs corresponds to the `(n + 1)`th Fibonacci number, we increment `n` by 1.
8. We apply Binet's Formula:
   `F(n) = (phi^n - psi^n) / sqrt(5)`
   which directly computes the required Fibonacci number.
9. Because floating-point calculations may introduce small precision errors, we use `round()` to obtain the nearest integer. The time complexity is `O(log n)` due to exponentiation, and the auxiliary space complexity is `O(1)` since only a few variables are used."""