#242. Valid Anagram 
"""Description
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false"""

#answer
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS,countT={},{}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
    
#example usage
solution = Solution()
print(solution.isAnagram("racecar", "carrace"))  # Output: True
print(solution.isAnagram("jar", "jam"))  # Output: False

"""WALKTHROUGH
1. We define a class Solution with a method isAnagram that takes two strings s and t as input.
2. We first check if the lengths of the two strings are different. If they are, we return False immediately, as they cannot be anagrams.
3. We initialize two empty dictionaries, countS and countT, to keep track of the frequency of each character in strings s and t, respectively.
4. We loop through the indices of the strings (from 0 to len(s)-1).
5. Inside the loop, for each character in string s, we update its count in the countS dictionary. We use the get method to retrieve the current count (defaulting to 0 if the character is not yet in the dictionary) and increment it by 1.
6. We do the same for string t, updating the countT dictionary.
7. After populating both dictionaries, we compare them. If they are equal, it means both strings have the same characters with the same frequencies, and we return True. Otherwise, we return False.
"""