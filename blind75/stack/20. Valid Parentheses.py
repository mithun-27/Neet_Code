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
    
#example usage
solution = Solution()
print(solution.isValid("()"))      # True
print(solution.isValid("()[]{}"))  # True
print(solution.isValid("(]"))      # False

"""walkthrough the code:
1. We initialize an empty stack to keep track of the opening brackets and a dictionary `closeToOpen` to map closing brackets to their corresponding opening brackets.
2. We iterate through each character `c` in the string `s`.
3. If `c` is a closing bracket (i.e., it exists in the `closeToOpen` dictionary), we check if the stack is not empty and if the top of the stack matches the corresponding opening bracket. If it does, we pop the top of the stack. Otherwise, we return False since it means there is a mismatch.
4. If `c` is not a closing bracket, it must be an opening bracket, so we push it onto the stack.
5. After iterating through all characters, we check if the stack is empty. If it is empty, it means all brackets were matched correctly, and we return True. If the stack is not empty, it means there are unmatched opening brackets, and we return False. 
6. The time complexity of this solution is O(n), where n is the length of the string `s`, since we need to iterate through each character once. The space complexity is also O(n) in the worst case, if all characters in `s` are opening brackets and we need to store them all in the stack.
"""