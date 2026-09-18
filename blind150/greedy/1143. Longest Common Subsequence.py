#1143. Longest Common Subsequence
"""Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters."""

#answer:
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        dp = [0] * (len(text2) + 1)

        for i in range(len(text1) - 1, -1, -1):
            prev = 0
            for j in range(len(text2) - 1, -1, -1):
                temp = dp[j]
                if text1[i] == text2[j]:
                    dp[j] = 1 + prev
                else:
                    dp[j] = max(dp[j], dp[j + 1])
                prev = temp

        return dp[0]

#example:
"""Input
text1 =
"abcde"
text2 =
"ace"
Output
3
Expected
3"""


"""Walkthrough:
1. We want to find the length of the Longest Common Subsequence (LCS) between `text1` and `text2`, where a subsequence preserves the relative order of characters but does not need to be contiguous.
2. The classic DP solution defines `dp[i][j]` as the length of the LCS between `text1[i:]` and `text2[j:]`.
3. Since each DP state depends only on the current row and the next row, we can optimize the space complexity from `O(m × n)` to `O(n)` using a single DP array.
4. To further reduce memory usage, the code ensures that `text2` is the shorter string, so the DP array size is minimized.
5. We create a DP array of size `len(text2) + 1`, initialized with zeros. The extra position represents the base case where one string has been fully processed.
6. We process both strings from right to left because each state depends on suffixes that have already been computed.
7. For every pair of characters `(text1[i], text2[j])`, if the characters match, we extend a common subsequence and set `dp[j] = 1 + prev`, where `prev` stores the old diagonal value corresponding to `dp[i+1][j+1]`.
8. If the characters do not match, we choose the better option between skipping a character from `text1` or skipping a character from `text2`, so `dp[j] = max(dp[j], dp[j + 1])`.
9. During each iteration, `temp` stores the old value of `dp[j]` before it is updated, and `prev` is updated to simulate the diagonal value needed for the next calculation.
10. By continuously updating the DP array from right to left, we effectively simulate the full 2D DP table using only one row of memory.
11. After processing all characters, `dp[0]` contains the length of the Longest Common Subsequence between the two strings.
12. The time complexity is `O(m × n)` where `m` and `n` are the lengths of the two strings, and the auxiliary space complexity is `O(min(m, n))` because only one DP array is stored."""