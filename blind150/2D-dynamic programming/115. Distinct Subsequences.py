#115. Distinct Subsequences
"""Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

 

Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit
Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
babgbag
babgbag
babgbag
babgbag
babgbag
 

Constraints:

1 <= s.length, t.length <= 1000
s and t consist of English letters.
 
"""

#answer:
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [0] * (n + 1)

        dp[n] = 1
        for i in range(m - 1, -1, -1):
            prev = 1
            for j in range(n - 1, -1, -1):
                res = dp[j]
                if s[i] == t[j]:
                    res += prev

                prev = dp[j]
                dp[j] = res

        return dp[0]

#example:
"""Input
s =
"rabbbit"
t =
"rabbit"
Output
3
Expected
3
"""

"""Walkthrough:
1. We want to find the number of distinct subsequences of `s` that are equal to `t`.
2. A subsequence is formed by deleting zero or more characters from `s` without changing the order of the remaining characters.
3. Let:
   `dp[i][j]`
   represent the number of ways to form `t[j:]` using `s[i:]`.
4. The base case is:
   - If we have matched all characters of `t`, there is exactly one valid subsequence (choose nothing more).
   - Therefore:
     `dp[*][n] = 1`
     where `n = len(t)`.
5. Instead of storing the entire 2D DP table, this solution uses a 1D DP array to optimize space.
6. We initialize:
   `dp[n] = 1`
   because an empty target string can always be formed.
7. We process `s` from right to left. For each character `s[i]`, we process `t` from right to left.
8. For every position `(i, j)`:
   - First, we consider skipping `s[i]`.
     This contributes:
     `dp[j]`
   - If `s[i] == t[j]`, we can also use this character to match `t[j]`.
     This contributes:
     `prev`
     where `prev` stores the old value of `dp[j+1]` (the diagonal value in the original 2D DP table).
9. Therefore:
   ```python
   if s[i] == t[j]:
       dp[j] = dp[j] + prev"""