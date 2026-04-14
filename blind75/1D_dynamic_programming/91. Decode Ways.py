#91. Decode Ways
"""You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:

"1" -> 'A'

"2" -> 'B'

...

"25" -> 'Y'

"26" -> 'Z'

However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes ("2" and "5" vs "25").

For example, "11106" can be decoded into:

"AAJF" with the grouping (1, 1, 10, 6)
"KJF" with the grouping (11, 10, 6)
The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).
Note: there may be strings that are impossible to decode.

Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return 0.

The test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: s = "12"

Output: 2

Explanation:

"12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:

Input: s = "226"

Output: 3

Explanation:

"226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:

Input: s = "06"

Output: 0

Explanation:

"06" cannot be mapped to "F" because of the leading zero ("6" is different from "06"). In this case, the string is not a valid encoding, so return 0.

 

Constraints:

1 <= s.length <= 100
s contains only digits and may contain leading zero(s)."""

#answer
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = dp2 = 0
        dp1 = 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp = 0
            else:
                dp = dp1

            if i + 1 < len(s) and (s[i] == "1" or
               s[i] == "2" and s[i + 1] in "0123456"
            ):
                dp += dp2
            dp, dp1, dp2 = 0, dp, dp1
        return dp1
    
#example
solution = Solution()
print(solution.numDecodings("12"))  # Output: 2
print(solution.numDecodings("226"))  # Output: 3
print(solution.numDecodings("06"))  # Output: 0
print(solution.numDecodings("10"))  # Output: 1

"""walkthrough
1. We initialize three variables `dp`, `dp1`, and `dp2` to keep track of the number of ways to decode the string at different positions. `dp1` is initialized to 1 because there is one way to decode an empty string.
2. We iterate through the string `s` from the end to the beginning. For each character, we check if it is '0'. If it is, we set `dp` to 0 because '0' cannot be decoded on its own. Otherwise, we set `dp` to `dp1`, which represents the number of ways to decode the substring starting from the next character.
3. We then check if the current character and the next character form a valid two-digit code (i.e., "10" to "26"). If they do, we add `dp2` to `dp`, which represents the number of ways to decode the substring starting from the character after the next one.            
4. Finally, we update `dp`, `dp1`, and `dp2` for the next iteration. `dp` is set to 0, `dp1` is set to the current value of `dp`, and `dp2` is set to the previous value of `dp1`.      
5. After the loop, we return `dp1`, which contains the total number of ways to decode the entire string.    
6. The time complexity of this solution is O(n), where n is the length of the input string `s`, and the space complexity is O(1) since we are using only a constant amount of extra space.  
"""