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
    
#example 1:
s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s)) # Output: 3
#example 2:
s = "bbbbb"
print(Solution().lengthOfLongestSubstring(s)) # Output: 1
#example 3:
s = "pwwkew"
print(Solution().lengthOfLongestSubstring(s)) # Output: 3

"""walkthrough:
1. We initialize a set called charSet to keep track of the unique characters in the current substring, a left pointer l to indicate the start of the substring, and a variable res to store the length of the longest substring found.  
2. We iterate through the string s using a right pointer r. For each character at index r, we check if it is already in charSet. If it is, it means we have a duplicate character in our current substring. In this case, we enter a while loop where we remove characters from charSet starting from the left pointer l until we remove the duplicate character. We also move the left pointer l to the right by one position each time we remove a character. 
3. After ensuring that the current character at index r is not in charSet, we add it to charSet and calculate the length of the current substring (which is r - l + 1) and update res if this length is greater than the current value of res.  
4. We continue this process until we have iterated through the entire string. Finally, we return res, which contains the length of the longest substring without repeating characters.
5. The time complexity of this algorithm is O(n) since we traverse the string at most once, and the space complexity is O(min(m, n)) where m is the size of the character set and n is the length of the string, because in the worst case, we may have to store all characters in charSet.    """  