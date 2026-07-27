#22. Generate Parentheses
"""Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8"""

#answer
class Solution:
    def generateParenthesis(self, n):
        res = [[] for _ in range(n+1)]
        res[0] = [""]

        for k in range(n + 1):
            for i in range(k):
                for left in res[i]:
                    for right in res[k-i-1]:
                        res[k].append("(" + left + ")" + right)

        return res[-1]

#example
"""Example 1:

Input: n = 1

Output: ["()"]
Example 2:

Input: n = 3

Output: ["((()))","(()())","(())()","()(())","()()()"]"""

"""Walkthrough:
1. We want to generate all possible combinations of `n` pairs of parentheses such that every combination is well-formed (balanced).
2. We use a backtracking (depth-first search) approach to build each combination one character at a time while maintaining two counters: the number of opening parentheses `(` used and the number of closing parentheses `)` used.
3. At each recursive call, we first check if the current combination has reached a length of `2 × n`. If it has, we have formed a valid combination, so we add it to the result list.
4. If the number of opening parentheses used is less than `n`, we can safely add another `(` and continue exploring recursively.
5. If the number of closing parentheses used is less than the number of opening parentheses used, we can add a `)` to maintain a valid sequence and continue the search.
6. We never allow the number of closing parentheses to exceed the number of opening parentheses because that would create an invalid combination.
7. After exploring each choice, we backtrack by removing the last added parenthesis, allowing us to explore other possible combinations.
8. The algorithm continues until every valid combination has been generated exactly once. Since invalid paths are pruned early, the search is much more efficient than generating all possible strings of parentheses.
9. The time complexity is `O(4^n / √n)` because the number of valid parentheses combinations is the `n`th Catalan number, while the auxiliary space complexity is `O(n)` for the recursion stack and the current string (excluding the output list)."""