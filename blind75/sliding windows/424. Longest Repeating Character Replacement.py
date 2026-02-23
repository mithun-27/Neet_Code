#424. Longest Repeating Character Replacement
"""You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length"""

#answer
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res
    
#example usage
solution = Solution()   
print(solution.characterReplacement("ABAB", 2))  # Output: 4
print(solution.characterReplacement("AABABBA", 1))  # Output: 4

"""walkthrough the code:
1. We initialize a dictionary `count` to keep track of the frequency of each character in the current window, a variable `res` to store the length of the longest valid substring found, a left pointer `l` to indicate the start of the window, and a variable `maxf` to store the maximum frequency of any character in the current window.
2. We iterate through the string `s` using a right pointer `r`. For each character at index `r`, we update its frequency in the `count` dictionary and update `maxf` to be the maximum frequency of any character in the current window.
3. We then check if the current window size minus `maxf` is greater than `k`. If it is, it means we need to shrink the window from the left by moving the left pointer `l` to the right and updating the frequency of the character at index `l` in the `count` dictionary. 
4. After ensuring that the current window is valid (i.e., it can be made to have all the same characters with at most `k` replacements), we update the result `res` with the maximum length found so far, which is calculated as `r - l + 1`.   
5. Finally, we return the value of `res`, which contains the length of the longest substring that can be formed with the same letter after at most `k` replacements.    
This algorithm runs in O(n) time complexity, where n is the length of the string `s`, since each character is visited at most twice (once by the right pointer and once by the left pointer). The space complexity is O(1) since we are only storing the frequency of uppercase English letters, which is a fixed size of 26.  
"""