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
1. We want to find the length of the Longest Common Subsequence (LCS) between `text1` and `text2`. A subsequence is formed by deleting characters without changing the relative order of the remaining characters.
2. The classic Dynamic Programming solution uses a 2D table where:
   `dp[i][j]` = length of the LCS between `text1[i:]` and `text2[j:]`.
3. Since each DP state depends only on the current row and the next row, we can optimize the space complexity from `O(m × n)` to `O(n)` by using a single array.
4. To minimize memory usage, the code ensures that `text2` is the shorter string. This makes the DP array as small as possible.
5. We create a DP array of size `len(text2) + 1`, initialized with zeros. Initially, the LCS involving an empty suffix is `0`.
6. We process both strings from right to left because each state depends on values corresponding to future indices.
7. For every character pair `(text1[i], text2[j])`:
   - If the characters match, we extend the common subsequence:
     `dp[j] = 1 + prev`
     where `prev` stores the value of the diagonal cell (`dp[i+1][j+1]`) from the original 2D DP table.
   - If the characters do not match, we choose the better option:
     `dp[j] = max(dp[j], dp[j+1])`
     representing either skipping a character from `text1` or from `text2`.
8. The variable `prev` is updated during each iteration to simulate the diagonal value from the previous row, allowing the 2D DP table to be compressed into a single array.
9. After processing all characters, `dp[0]` contains the length of the Longest Common Subsequence. The time complexity is `O(m × n)`, where `m` and `n` are the lengths of the two strings, and the auxiliary space complexity is `O(min(m, n))` because only one DP array is stored."""