#76. Minimum Window Substring
"""Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters."""

#answer
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
    
#example 1:
s = "ADOBECODEBANC" 
t = "ABC"   
print(Solution().minWindow(s, t)) # Output: "BANC"
#example 2:
s = "a"
t = "a"
print(Solution().minWindow(s, t)) # Output: "a"
#example 3:
s = "a"
t = "aa"
print(Solution().minWindow(s, t)) # Output: ""

"""walkthrough:
1. We first check if t is an empty string. If it is, we return an empty string since there are no characters to include in the window.
2. We create two dictionaries, countT and window, to keep track of the character counts in t and the current window of s, respectively. We populate countT with the frequency of each character in t.
3. We initialize two variables, have and need, to keep track of how many unique characters from t we have in the current window and how many unique characters we need to have, respectively. We also initialize res and resLen to keep track of the minimum window found so far.
4. We use a sliding window approach with two pointers, l and r, to traverse through s. For each character at index r, we add it to the window dictionary and check if it matches the required count in countT. If it does, we increment have.
5. We then enter a while loop that continues as long as have is equal to need, which means we have all the required characters in the current window. Inside the loop, we check if the current window is smaller than the previously recorded minimum window and update res and resLen accordingly.
6. We then remove the character at index l from the window and check if this causes us to lose a required character. If it does, we decrement have. We then move the left pointer l to the right to continue searching for smaller windows.
7. After the loop, we return the minimum window substring found, or an empty string if no valid window was found.
"""