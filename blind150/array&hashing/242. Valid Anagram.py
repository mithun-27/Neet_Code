#242. Valid Anagram
"""Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters."""

#answer
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
    
#example 1:
s = "anagram"
t = "nagaram"
solution = Solution()
print(solution.isAnagram(s, t)) # Output: true

#example 2:
s = "rat"
t = "car"
solution = Solution()
print(solution.isAnagram(s, t)) # Output: false 

"""walkthrough:
1. We first check if the lengths of the two strings are different. If they are, we can immediately return false since anagrams must have the same length.                   
2. We then create two dictionaries, countS and countT, to count the frequency of each character in strings s and t, respectively. We iterate through each character in both strings simultaneously and update the counts in the dictionaries.
3. Finally, we compare the two dictionaries. If they are equal, it means that both strings have the same characters with the same frequencies, and we return true. Otherwise, we return false."""   
