#49. Group Anagrams
"""Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters."""

#answer
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
    
#example 1:
strs = ["eat","tea","tan","ate","nat","bat"]
solution = Solution()
print(solution.groupAnagrams(strs)) # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

#example 2:
strs = [""]
solution = Solution()
print(solution.groupAnagrams(strs)) # Output: [[""]]

#example 3:
strs = ["a"]
solution = Solution()   
print(solution.groupAnagrams(strs)) # Output: [["a"]]

"""walkthrough: 
1. We initialize a defaultdict of lists called res to store the grouped anagrams.
2. We iterate through each string s in the input list strs.
3. For each string s, we create a count list of size 26 initialized to 0, which will be used to count the frequency of each character in the string.
4. We iterate through each character c in the string s and update the count list by incrementing the count at the index corresponding to the character (using ord(c) - ord('a') to get the index).
5. We convert the count list to a tuple and use it as a key in the res dictionary to append the original string s to the list of anagrams corresponding to that key.
6. Finally, we return the values of the res dictionary as a list, which will contain the grouped anagrams. Each group of anagrams will be a list of strings that are anagrams of each other.""" 
