#131. Palindrome Partitioning
"""Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters."""

#answer 
class Solution:

    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for l in range(1, n + 1):
            for i in range(n - l + 1):
                dp[i][i + l - 1] = (s[i] == s[i + l - 1] and
                                    (i + 1 > (i + l - 2) or
                                    dp[i + 1][i + l - 2]))

        def dfs(i):
            if i >= n:
                return [[]]

            ret = []
            for j in range(i, n):
                if dp[i][j]:
                    nxt = dfs(j + 1)
                    for part in nxt:
                        cur = [s[i : j + 1]] + part
                        ret.append(cur)
            return ret

        return dfs(0)

#example 1
"""Input: s = "aab"

Output: [["a","a","b"],["aa","b"]]"""

#example 2
"""Input: s = "a"

Output: [["a"]]"""

"""Walkthrough:
1. We want to partition the given string `s` into substrings such that every substring in the partition is a palindrome.
2. We use a backtracking (depth-first search) approach to explore every possible way of splitting the string into substrings.
3. Starting from the current index, we try every possible substring that begins at that index. For each substring, we first check whether it is a palindrome.
4. If the substring is a palindrome, we add it to the current partition and recursively continue searching from the next index after the selected substring.
5. If the recursion reaches the end of the string, it means every character has been partitioned successfully into palindromic substrings, so we add a copy of the current partition to the result list.
6. After each recursive call, we backtrack by removing the last added substring. This allows us to explore other possible partitions without affecting previous results.
7. If a substring is not a palindrome, we skip it immediately because it cannot be part of a valid partition.
8. The algorithm continues until every possible partition has been explored. Backtracking ensures that all valid palindrome partitions are generated exactly once.
9. The time complexity is exponential in the worst case (`O(n × 2^n)`) because many possible partitions may need to be explored, and checking each substring for being a palindrome takes up to `O(n)` time. The auxiliary space complexity is `O(n)` for the recursion stack and the current partition (excluding the output list)."""