#678. Valid Parenthesis String
"""Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "(*)"
Output: true
Example 3:

Input: s = "(*))"
Output: true
Example 4:

Input: s = "("
Output: false
 

Constraints:

1 <= s.length <= 100
s[i] is '(', ')' or '*'."""


#answer:
class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0


#example:
"""Input
s =
"()"
Output
true
Expected
true"""


"""Walkthrough:
1. We want to determine whether the given string can form a valid parentheses sequence, where `'*'` can be treated as `'('`, `')'`, or an empty string.
2. A valid parentheses string must never have more closing parentheses than opening parentheses at any point, and the total number of opening and closing parentheses must match by the end.
3. Since `'*'` can represent multiple possibilities, we cannot track a single balance value. Instead, we maintain a range of possible unmatched opening parentheses.
4. We use two variables:
   - `leftMin` = minimum possible number of unmatched `'('`.
   - `leftMax` = maximum possible number of unmatched `'('`.
5. Initially, both values are `0` because no characters have been processed.
6. When we encounter `'('`, it definitely increases the number of unmatched opening parentheses, so both `leftMin` and `leftMax` are incremented by `1`.
7. When we encounter `')'`, it definitely closes an opening parenthesis, so both `leftMin` and `leftMax` are decremented by `1`.
8. When we encounter `'*'`, it can act as:
   - `')'`, decreasing the count,
   - `'('`, increasing the count,
   - or an empty string, leaving the count unchanged.
   Therefore, `leftMin` is decremented by `1` and `leftMax` is incremented by `1`.
9. If `leftMax` becomes negative at any point, it means even under the most optimistic interpretation there are more closing parentheses than opening parentheses.
10. In that case, forming a valid string is impossible, so we immediately return `False`.
11. If `leftMin` becomes negative, we reset it to `0` because we cannot have fewer than zero unmatched opening parentheses.
12. Resetting `leftMin` to `0` effectively means we use some `'*'` characters as empty strings or opening parentheses to avoid a negative balance.
13. As we process the string, the interval `[leftMin, leftMax]` represents all possible counts of unmatched opening parentheses that could exist at that position.
14. After processing every character, a valid parentheses string is possible only if zero unmatched opening parentheses is within the valid range.
15. This is equivalent to checking whether `leftMin == 0`.
16. If `leftMin` is `0`, then there exists at least one interpretation of all `'*'` characters that produces a balanced parentheses string, so we return `True`.
17. Otherwise, some opening parentheses remain unmatched, and we return `False`.
18. The key insight is that instead of exploring all interpretations of `'*'`, we track only the minimum and maximum possible number of unmatched opening parentheses.
19. This greedy range-based approach efficiently captures every valid possibility without backtracking.
20. The time complexity is `O(n)` because the string is processed once, and the auxiliary space complexity is `O(1)` since only two variables are maintained."""