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

#answer
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