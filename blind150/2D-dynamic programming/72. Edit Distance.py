#72. Edit Distance
"""Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
 

Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters."""


#answer:
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if m < n:
            m, n = n, m
            word1, word2 = word2, word1

        dp = [n - i for i in range(n + 1)]

        for i in range(m - 1, -1, -1):
            nextDp = dp[n]
            dp[n] = m - i
            for j in range(n - 1, -1, -1):
                temp = dp[j]
                if word1[i] == word2[j]:
                    dp[j] = nextDp
                else:
                    dp[j] = 1 + min(dp[j], dp[j + 1], nextDp)
                nextDp = temp
        return dp[0]

#example:
"""Input
word1 =
"horse"
word2 =
"ros"
Output
3
Expected
3
"""

"""Walkthrough:
1. We want to find the minimum number of operations required to convert `word1` into `word2`.
2. The allowed operations are:
   - Insert a character
   - Delete a character
   - Replace a character
3. This is the classic Edit Distance (Levenshtein Distance) problem.
4. Define:
   `dp[i][j]`
   as the minimum operations needed to convert:
   `word1[i:]` → `word2[j:]`.
5. Base cases:
   - If `word1` is exhausted, we must insert all remaining characters of `word2`.
   - If `word2` is exhausted, we must delete all remaining characters of `word1`.
6. The code first ensures that `word2` is the shorter string, allowing a smaller DP array and better space efficiency.
7. We initialize:
   ```python
   dp[j] = n - j"""