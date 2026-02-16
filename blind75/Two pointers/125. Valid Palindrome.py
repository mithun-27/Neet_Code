#125. Valid Palindrome

"""A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters."""

#answer
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
#example usage
solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
print(solution.isPalindrome("race a car"))  # Output: False
print(solution.isPalindrome(" "))  # Output: True

"""WALKTHROUGH
1. We define a class Solution with a method isPalindrome that takes a string s as input.
2. We initialize two pointers, l and r, to the start and end of the string, respectively.
3. We use a while loop to iterate as long as l is less than r.
4. Inside the loop, we use two nested while loops to skip over any non-alphanumeric characters. The first loop moves the left pointer l to the right until it points to an alphanumeric character, and the second loop moves the right pointer r to the left until it points to an alphanumeric character.  
5. After skipping non-alphanumeric characters, we compare the characters at the left and right pointers. We convert both characters to lowercase to ensure the comparison is case-insensitive. If the characters do not match, we return False, indicating that the string is not a palindrome. 
6. If the characters match, we move the left pointer l to the right and the right pointer r to the left, and continue the process until l is no longer less than r.     
7. If we exit the loop without finding any mismatches, we return True, indicating that the string is a palindrome.
8. We also define a helper method alphaNum that checks if a character is alphanumeric by comparing its ASCII values.
"""