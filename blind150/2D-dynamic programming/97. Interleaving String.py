#97. Interleaving String
"""Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m substrings respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

 

Example 1:


Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.
Example 3:

Input: s1 = "", s2 = "", s3 = ""
Output: true
 

Constraints:

0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lowercase English letters."""


#answer:
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        if n < m:
            s1, s2 = s2, s1
            m, n = n, m

        dp = [False for _ in range(n + 1)]
        dp[n] = True
        for i in range(m, -1, -1):
            nextDp = True if i == m else False
            for j in range(n, -1, -1):
                res = False if j < n else nextDp
                if i < m and s1[i] == s3[i + j] and dp[j]:
                    res = True
                if j < n and s2[j] == s3[i + j] and nextDp:
                    res = True
                dp[j] = res
                nextDp = dp[j]
        return dp[0]


"""Walkthrough:
1. We want to determine whether `s3` can be formed by interleaving the characters of `s1` and `s2` while preserving the relative order of characters within each string.
2. Before doing any computation, we check whether:
   len(s1) + len(s2) == len(s3)
   If not, forming `s3` is impossible, so we immediately return `False`.
3. This is a Dynamic Programming problem because at every position we can choose the next character from either `s1` or `s2`.
4. Define:
   `dp[i][j] = True`
   if the substring `s3[i+j:]` can be formed using:
   - `s1[i:]`
   - `s2[j:]`
5. The base case is:
   `dp[len(s1)][len(s2)] = True`
   because when both strings are exhausted, we have successfully formed all of `s3`.
6. Starting from the end of both strings and moving backward:
   - If `s1[i]` matches `s3[i+j]`, we can take a character from `s1`.
   - If `s2[j]` matches `s3[i+j]`, we can take a character from `s2`.
7. Therefore:
   ```python
   dp[i][j] =
       (s1[i] == s3[i+j] and dp[i+1][j])
       or
       (s2[j] == s3[i+j] and dp[i][j+1])"""