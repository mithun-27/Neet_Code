#139. Word Break
"""Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique."""

#answer
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, s, i, j):
        node = self.root
        for idx in range(i, j + 1):
            if s[idx] not in node.children:
                return False
            node = node.children[s[idx]]
        return node.is_word

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        t = 0
        for w in wordDict:
            t = max(t, len(w))

        for i in range(len(s), -1, -1):
            for j in range(i, min(len(s), i + t)):
                if trie.search(s, i, j):
                    dp[i] = dp[j + 1]
                    if dp[i]:
                        break

        return dp[0]
    
#example
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".

"""walkthrough:
1. We define a `TrieNode` class to represent each node in the trie, which contains a dictionary of children and a boolean flag to indicate if the node represents the end of a word.    
2. We define a `Trie` class to manage the trie structure, which includes methods for inserting words and searching for words in the trie.   
3. In the `Solution` class, we create a trie and insert all the words from the `wordDict` into it.
4. We initialize a dynamic programming array `dp` of size `len(s) + 1` with all values set to `False`, except for `dp[len(s)]` which is set to `True` to indicate that an empty string can be segmented.
5. We calculate the maximum length of the words in the `wordDict` to optimize our search.
6. We iterate through the string `s` from the end to the beginning, and for each position `i`, we check for all possible end positions `j` (up to the maximum word length) to see if the substring `s[i:j+1]` exists in the trie. If it does, we set `dp[i]` to the value of `dp[j + 1]`, which indicates whether the remaining substring can be segmented. If `dp[i]` becomes `True`, we break out of the inner loop to avoid unnecessary checks.
7. Finally, we return `dp[0]`, which indicates whether the entire string `s` can be segmented into words from the `wordDict`.
This approach efficiently checks for valid segmentations of the string `s` using a trie to store the dictionary words and a dynamic programming array to keep track of valid segmentations at each position in the string. By iterating from the end of the string to the beginning, we ensure that we can build up our solution based on previously computed results in the `dp` array.""" 
