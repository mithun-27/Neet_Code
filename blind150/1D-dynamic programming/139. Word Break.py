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

#answer:
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


#example:
"""Input
s =
"leetcode"
wordDict =
["leet","code"]
Output
true
Expected
true"""

#example:
"""Input
s =
"applepenapple"
wordDict =
["apple","pen"]
Output
true
Expected
true
"""


"""Walkthrough:
1. We want to determine whether the string `s` can be segmented into one or more words from the given dictionary `wordDict`.
2. To efficiently check whether a substring is a valid dictionary word, we first build a Trie (Prefix Tree) containing all words from `wordDict`.
3. Each Trie node stores its children characters and a flag `is_word` indicating whether a complete dictionary word ends at that node.
4. We create a Dynamic Programming array `dp` of size `len(s) + 1`, where:
   `dp[i] = True` means the substring starting at index `i` can be successfully segmented into dictionary words.
5. The base case is:
   `dp[len(s)] = True`
   because an empty string can always be segmented successfully.
6. To reduce unnecessary checks, we compute `t`, the length of the longest word in the dictionary. This ensures we never examine substrings longer than any possible dictionary word.
7. We process the string from right to left. For each starting index `i`, we try all possible ending indices `j` such that the substring length does not exceed `t`.
8. For every substring `s[i:j+1]`, we use the Trie's `search()` method to check whether it is a valid dictionary word. If it is, we look at `dp[j+1]` to determine whether the remaining suffix can also be segmented.
9. If both conditions are true, we set `dp[i] = True` and stop checking further substrings from index `i`. After filling the DP array, `dp[0]` tells us whether the entire string can be segmented. The time complexity is approximately `O(n × L²)`, where `n` is the string length and `L` is the maximum dictionary word length, and the auxiliary space complexity is `O(n + total_dictionary_characters)` for the DP array and Trie."""