#212. Word Search II
"""Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique."""

#answwer:
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

class Solution:
    def findWords(self, board, words):
        trie = Trie()
        for word in words:
            trie.insert(word)

        self.result = set()
        self.rows, self.cols = len(board), len(board[0])
        self.visited = set()

        def backtrack(r, c, node, path):
            if node.is_end_of_word:
                self.result.add(path)
                node.is_end_of_word = False 
            
            self.visited.add((r, c))
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < self.rows and 0 <= new_c < self.cols and (new_r, new_c) not in self.visited:
                    next_char = board[new_r][new_c]
                    if next_char in node.children:
                        backtrack(new_r, new_c, node.children[next_char], path + next_char)

            self.visited.remove((r, c))

        for r in range(self.rows):
            for c in range(self.cols):
                start_char = board[r][c]
                if start_char in trie.root.children:
                    backtrack(r, c, trie.root.children[start_char], start_char)

        return list(self.result)

#example 1 :
"""Input
board =
[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words =
["oath","pea","eat","rain"]
Output
["oath","eat"]
Expected
["oath","eat"]"""

#example 2:
"""Input
board =
[["a","b"],["c","d"]]
words =
["abcb"]
Output
[]
Expected
[]"""

"""Walkthrough:
1. We want to find all the words from the given `words` list that can be formed on the board by moving horizontally or vertically to adjacent cells without reusing the same cell in a single word.
2. Instead of searching for each word separately, we first build a Trie (Prefix Tree) containing all the words. This allows us to search for many words simultaneously while sharing common prefixes.
3. We iterate through every cell of the board and treat each cell as a possible starting position. From each cell, we perform a depth-first search (DFS) while traversing both the board and the Trie at the same time.
4. During the DFS, we first check whether the current board character exists as a child of the current Trie node. If it does not, we immediately stop exploring that path because no word in the Trie can start with the current prefix.
5. If the character exists, we move to the corresponding Trie node. If this Trie node marks the end of a word, we have found a valid word, so we add it to the result list and remove its end marker to avoid reporting the same word multiple times.
6. We temporarily mark the current board cell as visited (for example, by replacing it with `'#'`) so that it cannot be reused while constructing the current word. We then recursively explore the four adjacent directions: up, down, left, and right.
7. After exploring all possible directions, we restore the original character in the board (backtracking) so that the cell can be used in other search paths.
8. As an optimization, if a Trie node no longer has any children after a word has been found, we remove that node from its parent. This prunes unnecessary search paths and improves performance for the remaining DFS calls.
9. The algorithm continues until every cell has been explored. Using the Trie significantly reduces redundant searches compared to checking each word individually. The worst-case time complexity is `O(m × n × 4^L)`, where `L` is the maximum word length, although Trie pruning makes it much faster in practice. The auxiliary space complexity is `O(W × L)` for the Trie, where `W` is the number of words, plus `O(L)` for the recursion stack (excluding the output list)."""