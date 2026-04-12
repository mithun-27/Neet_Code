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

#answer
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
    
#example
solution = Solution()
print(solution.longestPalindrome("babad"))  # Output: "bab" or "aba"
print(solution.longestPalindrome("cbbd"))  # Output: "bb"
print(solution.longestPalindrome("a"))  # Output: "a"
print(solution.longestPalindrome("ac"))  # Output: "a" or "c"   

"""walkthrough
1. We define a helper function `manacher` that implements Manacher's algorithm to find the longest palindromic substring in linear time.
2. We transform the input string `s` by inserting a special character (e.g., '#') between each character and at the beginning and end of the string. This allows us to handle even-length palindromes uniformly with odd-length palindromes.
3. We initialize an array `p` to store the radius of the longest palindrome centered at each position in the transformed string, and two pointers `l` and `r` to keep track of the rightmost palindrome found so far.
4. We iterate through each character in the transformed string, updating the `p` array based on the previously found palindromes and expanding around the current center to find the longest palindrome.
5. After processing the transformed string, we find the maximum value in the `p` array, which gives us the length of the longest palindrome and its center index. We then calculate the starting index of the longest palindrome in the original string and return the corresponding substring.
6. The time complexity of this solution is O(n) due to the linear traversal of the transformed string, and the space complexity is O(n) for the `p` array and the transformed string.
"""