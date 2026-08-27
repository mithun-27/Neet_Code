#5. Longest Palindromic Substring
"""Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters."""

#answer:
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def manacher(s):
            t = '#' + '#'.join(s) + '#'
            n = len(t)
            p = [0] * n
            l, r = 0, 0
            for i in range(n):
                p[i] = min(r - i, p[l + (r - i)]) if i < r else 0
                while (i + p[i] + 1 < n and i - p[i] - 1 >= 0
                       and t[i + p[i] + 1] == t[i - p[i] - 1]):
                    p[i] += 1
                if i + p[i] > r:
                    l, r = i - p[i], i + p[i]
            return p

        p = manacher(s)
        resLen, center_idx = max((v, i) for i, v in enumerate(p))
        resIdx = (center_idx - resLen) // 2
        return s[resIdx : resIdx + resLen]

#example:
"""Input
s =
"babad"
Output
"aba"
Expected
"bab"""

#walkthrough:
"""
1. We want to find the longest palindromic substring in the given string. A palindrome reads the same forward and backward.
2. A naive approach would expand around every center, resulting in `O(n²)` time complexity. This solution uses Manacher's Algorithm, which solves the problem in linear time `O(n)`.
3. First, we transform the string by inserting `'#'` between every character and at both ends. For example:
   `"abba"` → `"#a#b#b#a#"`
   This allows us to treat odd-length and even-length palindromes uniformly.
4. We create an array `p` where `p[i]` stores the radius of the palindrome centered at index `i` in the transformed string.
5. We maintain two pointers:
   - `l` = left boundary of the rightmost palindrome found so far.
   - `r` = right boundary of the rightmost palindrome found so far.
6. For each position `i`, if `i` lies inside the current palindrome (`i < r`), we use the mirror property of palindromes to initialize `p[i]` without rechecking all characters. This avoids redundant work.
7. We then try to expand the palindrome centered at `i` by comparing characters on both sides. As long as the characters match, we increase the radius `p[i]`.
8. If the palindrome centered at `i` extends beyond the current right boundary `r`, we update `l` and `r` to represent this new rightmost palindrome.
9. After processing all positions, the maximum value in `p` represents the longest palindrome radius. Using its center index and radius, we convert the position back to the original string and return the corresponding substring. The time complexity is `O(n)` because each character is processed at most a constant number of times, and the auxiliary space complexity is `O(n)` for the transformed string and radius array."""