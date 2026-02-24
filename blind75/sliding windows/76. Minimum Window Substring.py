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
    
#example usage
solution = Solution()
print(solution.minWindow("ADOBECODEBANC", "ABC"))  # Output: "BANC"
print(solution.minWindow("a", "a"))  # Output: "a"
print(solution.minWindow("a", "aa"))  # Output: ""  

"""walkthrough the code:
1. We first check if the string `t` is empty. If it is, we return an empty string since there are no characters to include in the window.   
2. We initialize two dictionaries: `countT` to store the frequency of each character in `t`, and `window` to store the frequency of characters in the current window of `s`. We populate `countT` by iterating through each character in `t` and counting its occurrences.  
3. We initialize two variables `have` and `need` to keep track of how many unique characters from `t` we have in the current window and how many unique characters we need to have, respectively. We also initialize `res` to store the indices of the minimum window found and `resLen` to store the length of that window. We set `l` to 0 to represent the left pointer of our sliding window.   
4. We iterate through the string `s` using a right pointer `r`. For each character at index `r`, we update its frequency in the `window` dictionary. If this character is also in `countT` and its frequency in the current window matches the required frequency in `countT`, we increment the `have` counter. 
5. We then check if `have` is equal to `need`, which means we have a valid window that contains all characters from `t`. If it is valid, we enter a while loop to try to shrink the window from the left. Inside the loop, we check if the current window size is smaller than the previously recorded minimum window size. If it is, we update `res` with the current indices and `resLen` with the new minimum length. We then decrement the frequency of the character at index `l` in the `window` dictionary. If this character is in `countT` and its frequency in the current window falls below the required frequency, we decrement the `have` counter. Finally, we move the left pointer `l` to the right by incrementing it.     
6. After the loop, we check if `resLen` is still infinity, which means we did not find any valid window. If it is not infinity, we return the substring of `s` from index `l` to `r + 1` using the indices stored in `res`. Otherwise, we return an empty string.   
This algorithm runs in O(m + n) time complexity, where m is the length of string `s` and n is the length of string `t`, since we are iterating through both strings at most once. The space complexity is O(m + n) in the worst case, if all characters in `s` and `t` are unique, due to the dictionaries used to store character frequencies. However, since we are only dealing with uppercase and lowercase English letters, the space complexity can be considered O(1) as well.  
"""