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

#answer
class Solution:
    def climbStairs(self, n: int) -> int:
        sqrt5 = math.sqrt(5)
        phi = (1 + sqrt5) / 2
        psi = (1 - sqrt5) / 2
        n += 1
        return round((phi**n - psi**n) / sqrt5)


"""walkthrough
1. We calculate the square root of 5 and store it in the variable `sqrt5`.
2. We calculate the golden ratio `phi` using the formula (1 + sqrt5) / 2.
3. We calculate the conjugate of the golden ratio `psi` using the formula (1 - sqrt5) / 2.
4. We increment `n` by 1 to account for the base case of 0 steps.
5. We use Binet's formula to calculate the nth Fibonacci number, which gives us the number of distinct ways to climb to the top. The formula is (phi^n - psi^n) / sqrt5.
6. We round the result to the nearest integer and return it as the final answer.
The time complexity of this solution is O(1) since we are performing a constant number of operations, and the space complexity is also O(1) since we are using a constant amount of space to store the variables.   
"""