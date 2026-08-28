#647. Palindromic Substrings
"""Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters."""

#answer:
class Solution:
    def countSubstrings(self, s: str) -> int:

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
        res = 0
        for i in p:
            res += (i + 1) // 2
        return res

    
#example 1 :
"""Input
s =
"abc"
Output
3
Expected
3""" 

#example 2 :
"""Input
s =
"aaa"
Output
6
Expected
6
"""

#walthrough:
"""
1. We want to count all palindromic substrings in the given string. A palindrome is a substring that reads the same forward and backward.
2. Instead of checking every possible substring, this solution uses Manacher's Algorithm, which finds information about all palindromes in linear time.
3. First, we transform the string by inserting `'#'` between every character and at both ends. For example:
   `"aba"` → `"#a#b#a#"`
   This allows odd-length and even-length palindromes to be handled uniformly.
4. We create an array `p` where `p[i]` stores the radius of the longest palindrome centered at position `i` in the transformed string.
5. We maintain two pointers:
   - `l` = left boundary of the current rightmost palindrome.
   - `r` = right boundary of the current rightmost palindrome.
6. For each position `i`, if it lies inside the current palindrome (`i < r`), we use the mirror position to initialize `p[i]`. This avoids recomputing information that is already known.
7. We then expand around the center `i` by comparing characters on both sides. As long as they match, we increase the palindrome radius `p[i]`.
8. Once all centers are processed, the array `p` contains the radius of the largest palindrome centered at every position. For each radius value `i`, the number of palindromic substrings contributed by that center is `(i + 1) // 2`.
9. We sum `(radius + 1) // 2` for all centers in `p` to obtain the total number of palindromic substrings. The time complexity is `O(n)` because Manacher's Algorithm processes each character a constant number of times, and the auxiliary space complexity is `O(n)` for the transformed string and radius array."""