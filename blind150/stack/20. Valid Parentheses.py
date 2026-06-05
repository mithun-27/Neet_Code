#20. Valid Parentheses
"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'."""

#answer
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
    
#example 1:
s = "()"
print(Solution().isValid(s)) # Output: true
#example 2:
s = "()[]{}"
print(Solution().isValid(s)) # Output: true
#example 3:
s = "(]"
print(Solution().isValid(s)) # Output: false    
#example 4:
s = "([])"
print(Solution().isValid(s)) # Output: true

"""walkthrough:
1. We initialize an empty stack to keep track of the opening brackets and a dictionary to map each closing bracket to its corresponding opening bracket.
2. We iterate through each character c in the input string s. If c is a closing bracket, we check if the stack is not empty and if the top of the stack is the corresponding opening bracket. If it is, we pop the top of the stack. If it is not, we return False because it means there is a mismatch.
3. If c is an opening bracket, we simply push it onto the stack.
4. After iterating through all characters in the string, we check if the stack is empty. If it is empty, it means all brackets were matched correctly, and we return True. If it is not empty, it means there are unmatched opening brackets, and we return False.  
This algorithm runs in O(n) time, where n is the length of the input string, because we need to iterate through each character once. The space complexity is also O(n) in the worst case, if all characters are opening brackets and we need to store them in the stack.    
"""