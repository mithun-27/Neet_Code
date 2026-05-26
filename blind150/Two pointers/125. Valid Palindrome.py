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
    
#example 1:
solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama")) # Output: true
#example 2:
print(solution.isPalindrome("race a car")) # Output: false
#example 3:
print(solution.isPalindrome(" ")) # Output: true

"""walkthrough:
1. We initialize two pointers, l and r, to the start and end of the string, respectively.           
2. We use a while loop to move the pointers towards each other until they meet. Inside the loop, we skip any non-alphanumeric characters by moving the pointers accordingly.    
3. After skipping non-alphanumeric characters, we compare the characters at the l and r pointers (ignoring case). If they are not equal, we return False, indicating that the string is not a palindrome.
4. If the characters are equal, we move both pointers towards the center and continue the process until they meet. If we exit the loop without finding any mismatches, we return True, indicating that the string is a palindrome.
This algorithm runs in O(n) time, where n is the length of the string, because we potentially check each character once. The space complexity is O(1) since we are using only a constant amount of extra space for the pointers and the helper function. """    
