# 49. Group Anagrams
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
from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())

#example usage
solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))  # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
print(solution.groupAnagrams([""]))  # Output: [[""]]
print(solution.groupAnagrams(["a"]))  # Output: [["a"]]

"""WALKTHROUGH
1. We import defaultdict from the collections module to facilitate grouping anagrams.
2. We define a class Solution with a method groupAnagrams that takes a list of strings strs as input.
3. We initialize a defaultdict called res, where each key will map to a list of strings (the anagrams).
4. We iterate through each string s in the input list strs.
5. For each string, we create a count list of size 26 (for each letter in the English alphabet) initialized to zero.
6. We then iterate through each character c in the string s, updating the count list by incrementing the corresponding index based on the character's ASCII value.
7. We convert the count list to a tuple (since lists are not hashable and cannot be used as dictionary keys) and use it as a key in the res dictionary, appending the original string s to the list of anagrams for that key.   
8. After processing all strings, we return the values of the res dictionary as a list, which contains groups of anagrams.
"""