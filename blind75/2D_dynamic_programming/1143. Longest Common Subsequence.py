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
#answer
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
    
#example 1:
text1 = "abcde" 
text2 = "ace"
solution = Solution()
print(solution.longestCommonSubsequence(text1, text2))  # Output: 3
#example 2:
text1 = "abc"
text2 = "abc"
solution = Solution()   
print(solution.longestCommonSubsequence(text1, text2))  # Output: 3
#example 3:
text1 = "abc"
text2 = "def"
solution = Solution()
print(solution.longestCommonSubsequence(text1, text2))  # Output: 0

"""walkthrough the code:
1. We first check if `text1` is shorter than `text2`. If it is, we swap them to ensure that `text1` is the longer string. This optimization helps reduce the space complexity of our dynamic programming solution.  
2. We initialize a one-dimensional list `dp` of size `len(text2) + 1` with all values set to 0. This list will be used to store the lengths of the longest common subsequences for substrings of `text1` and `text2`.   
3. We iterate through `text1` in reverse order (from the last character to the first). For each character in `text1`, we initialize a variable `prev` to 0, which will hold the value of `dp[j]` from the previous iteration of the inner loop. This is necessary because we will be updating `dp[j]` in place, and we need to keep track of the previous value for our calculations.   
4. We then iterate through `text2` in reverse order. For each character in `text2`, we store the current value of `dp[j]` in a temporary variable `temp` before updating it. If the characters at the current indices of `text1` and `text2` match, we set `dp[j]` to `1 + prev`, which means we have found a common character and we can extend the longest common subsequence by 1. If they do not match, we set `dp[j]` to the maximum of `dp[j]` and `dp[j + 1]`, which means we take the longest subsequence found so far without including the current character of either string. After processing each character of `text2`, we update `prev` to the value stored in `temp` for the next iteration. 
5. After processing all characters of both strings, the length of the longest common subsequence will be stored in `dp[0]`, which we return as the final result.    
The time complexity of this solution is O(m * n), where m and n are the lengths of `text1` and `text2`, respectively. The space complexity is O(n) due to the use of the one-dimensional `dp` list. This is an efficient solution for the longest common subsequence problem, especially when one string is significantly shorter than the other.   
"""