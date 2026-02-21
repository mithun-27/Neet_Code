#3. Longest Substring Without Repeating Characters
"""Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces."""

#answer
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
    
#example usage
solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
print(solution.lengthOfLongestSubstring("bbbbb"))  # Output: 1  
print(solution.lengthOfLongestSubstring("pwwkew"))  # Output: 3

"""walkthrough the code:
1. We initialize a set called `charSet` to keep track of the unique characters in the current substring, a left pointer `l` to indicate the start of the substring, and a variable `res` to store the length of the longest substring found.
2. We iterate through the string `s` using a right pointer `r`. For each character at index `r`, we check if it is already in `charSet`. If it is, it means we have a duplicate character, and we need to move the left pointer `l` to the right until we remove the duplicate character from `charSet`.        
3. After ensuring that the character at index `r` is not in `charSet`, we add it to the set and update the result `res` with the maximum length found so far, which is calculated as `r - l + 1`.   
4. Finally, we return the value of `res`, which contains the length of the longest substring without repeating characters.  
This algorithm runs in O(n) time complexity, where n is the length of the string `s`, since each character is visited at most twice (once by the right pointer and once by the left pointer). The space complexity is O(min(m, n)), where m is the size of the character set and n is the length of the string, since we are storing characters in a set. In practice, this is often O(1) if we assume a fixed character set (like ASCII).  
"""