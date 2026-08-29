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

#answer:
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

#example 1 :
"""Input
s =
"12"
Output
2
Expected
2"""

#example 2 :
"""Input
s =
"226"
Output
3
Expected
3
"""

#example 3 :
"""Input
s =
"06"
Output
0
Expected
0
"""

#walkthrough:
"""Walkthrough:
1. We want to find the number of ways to decode the string, where:
   - `'1' -> 'A'`
   - `'2' -> 'B'`
   - ...
   - `'26' -> 'Z'`
2. At each position, we have two possible choices:
   - Decode the current digit alone (if it is not `'0'`).
   - Decode the current digit together with the next digit (if they form a valid number from `10` to `26`).
3. This naturally leads to a Dynamic Programming problem where:
   `dp[i] = number of ways to decode the substring starting at index i`.
4. Instead of storing an entire DP array, this solution uses three variables:
   - `dp1` = result for `dp[i+1]`
   - `dp2` = result for `dp[i+2]`
   - `dp`  = current result for `dp[i]`
5. We process the string from right to left because each state depends on future positions.
6. If the current character is `'0'`, it cannot be decoded by itself, so the number of ways is `0`.
7. Otherwise, we can decode the current digit alone, so we start with:
   `dp = dp1`
   because the remaining substring can be decoded in `dp1` ways.
8. Next, we check whether the current digit and the next digit form a valid two-digit number (`10` to `26`). If they do, we add:
   `dp += dp2`
   because decoding those two digits together leaves the substring starting at `i+2`.
9. After calculating the current answer, we shift the DP variables:
   - `dp2 = dp1`
   - `dp1 = dp`
   and continue moving left. When the loop finishes, `dp1` contains the total number of valid decodings. The time complexity is `O(n)` because each character is processed once, and the auxiliary space complexity is `O(1)` since only a few variables are used."""