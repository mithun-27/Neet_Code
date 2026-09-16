#10. Regular Expression Matching
"""Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
Return a boolean indicating whether the matching covers the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
 

Constraints:

1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match."""


#answer:
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [False] * (len(p) + 1)
        dp[len(p)] = True

        for i in range(len(s), -1, -1):
            dp1 = dp[len(p)]
            dp[len(p)] = (i == len(s))

            for j in range(len(p) - 1, -1, -1):
                match = i < len(s) and (s[i] == p[j] or p[j] == ".")
                res = False
                if (j + 1) < len(p) and p[j + 1] == "*":
                    res = dp[j + 2]
                    if match:
                        res |= dp[j]
                elif match:
                    res = dp1
                dp[j], dp1 = res, dp[j]

        return dp[0]

#examplle:
"""Input
s =
"aa"
p =
"a"
Output
false
Expected
false"""

#walkthrough:
"""Walkthrough:
1. We want to determine whether the string `s` matches the pattern `p`, where `'.'` matches any single character and `'*'` matches zero or more occurrences of the preceding character.
2. This is a Dynamic Programming problem because the answer for a position `(i, j)` depends on the answers of smaller suffixes of the string and pattern.
3. Let `dp[i][j]` represent whether the substring `s[i:]` matches the pattern `p[j:]`.
4. Instead of storing the full 2D DP table, this solution uses a 1D DP array to optimize space, where `dp[j]` represents the current row's value for pattern position `j`.
5. The base case is `dp[len(p)] = True`, meaning an empty string matches an empty pattern.
6. We process the string and pattern from right to left because each state depends on future positions.
7. For every pair `(i, j)`, we first check whether the current characters match:
   - `s[i] == p[j]`
   - or `p[j] == '.'`
8. If the next character in the pattern is `'*'`, we have two choices:
   - Ignore the current pattern character and `'*'` completely (`zero occurrences`), which corresponds to `dp[j + 2]`.
   - Use the current character if it matches, and stay at the same pattern position to potentially consume more characters, which corresponds to `dp[j]`.
9. If there is no `'*'`, then a valid match requires the current characters to match and the remaining suffixes to match as well, which corresponds to the diagonal DP value stored in `dp1`.
10. The result for each state is stored back into `dp[j]`, while `dp1` keeps track of the previous diagonal value needed for the next iteration.
11. By processing all positions from the end toward the beginning, we gradually build the answer for larger prefixes of the string and pattern.
12. After all states have been evaluated, `dp[0]` indicates whether the entire string matches the entire pattern. The time complexity is `O(len(s) × len(p))`, and the auxiliary space complexity is `O(len(p))` because only a single DP row is stored."""