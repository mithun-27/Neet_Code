#567. Permutation in String
"""Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters."""

#answer
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26
    
#example 1:
s1 = "ab"
s2 = "eidbaooo"
print(Solution().checkInclusion(s1, s2)) # Output: true
#example 2:
s1 = "ab"
s2 = "eidboaoo"
print(Solution().checkInclusion(s1, s2)) # Output: false

"""walkthrough:
1. We first check if the length of s1 is greater than the length of s2. If it is, we can immediately return false since s2 cannot contain a permutation of s1.  
2. We initialize two lists, s1Count and s2Count, of size 26 to count the frequency of each character in s1 and the current window of s2, respectively. We populate these lists for the first len(s1) characters of s2.  
3. We then count the number of matches between s1Count and s2Count. A match occurs when the frequency of a character in s1Count is equal to the frequency of that character in s2Count. We store this count in the variable matches.        
4. We use a sliding window approach to iterate through s2 starting from the index len(s1). For each character at index r, we first check if matches is equal to 26, which means all characters match and we can return true.    
5. We then update s2Count for the character at index r and check if this update creates a new match or breaks an existing match, updating the matches count accordingly.        
6. We also update s2Count for the character at index l (the left end of the window) and check if this update creates a new match or breaks an existing match, updating the matches count accordingly. We then move the left pointer l to the right by one position.         
7. We continue this process until we have iterated through the entire string s2. Finally, we return whether matches is equal to 26, which indicates that we found a permutation of s1 in s2.        
8. The time complexity of this algorithm is O(n) since we traverse the string s2 at most once, and the space complexity is O(1) since we are using fixed-size lists to count character frequencies.    """      
