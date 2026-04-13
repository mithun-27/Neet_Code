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

#answer
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
    
#example
solution = Solution()
print(solution.countSubstrings("abc"))  # Output: 3
print(solution.countSubstrings("aaa"))  # Output: 6
print(solution.countSubstrings("a"))  # Output: 1
print(solution.countSubstrings("ab"))  # Output: 2

"""walkthrough
1. We define a helper function `manacher` that implements Manacher's algorithm to find the longest palindromic substring in linear time.
2. We transform the input string `s` by inserting a special character (e.g., '#') between each character and at the beginning and end of the string. This allows us to handle even-length palindromes uniformly with odd-length palindromes.
3. We initialize an array `p` to store the radius of the longest palindrome centered at each position in the transformed string, and two pointers `l` and `r` to keep track of the rightmost palindrome found so far.
4. We iterate through each character in the transformed string, updating the `p` array based on the previously found palindromes and expanding around the current center to find the longest palindrome.
5. After processing the transformed string, we calculate the total number of palindromic substrings by summing up the contributions from each center. The number of palindromic substrings contributed by a center with radius `i` is `(i + 1) // 2`, which accounts for both odd and even length palindromes.  
6. The time complexity of this solution is O(n) due to the linear traversal of the transformed string, and the space complexity is O(n) for the `p` array and the transformed string.
"""