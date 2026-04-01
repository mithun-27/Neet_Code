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
    
#example usage
solution = Solution()
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
print(solution.findWords(board, words)) # Output: ["eat","oath"]

"""walkthrough the code:
1. We define a TrieNode class to represent each node in the trie, which contains a dictionary of children and a boolean flag to indicate if it represents the end of a word.    
2. We define a Trie class to manage the trie structure, with an insert method to add words to the trie. 
3. In the Solution class, we build the trie from the list of words and then use backtracking to explore the board.
4. The backtrack function checks if the current node represents the end of a word and adds it to the result set. It then explores adjacent cells recursively, ensuring that we do not revisit cells in the same path.   
5. Finally, we return the list of found words.  
This solution efficiently finds all valid words on the board by leveraging the trie structure to quickly check for prefixes and complete words, while using backtracking to explore potential paths on the board.   
6. The example usage demonstrates how to use the Solution class to find words on a given board, and the expected output is shown in the comments.   
7. The time complexity of this solution is O(M * N * 4^L) in the worst case, where M and N are the dimensions of the board and L is the length of the longest word. However, the trie helps to reduce unnecessary explorations, making it more efficient in practice. The space complexity is O(W * L) for storing the trie, where W is the number of words and L is the average length of the words.   
8. This approach is effective for handling the constraints provided, as it allows for efficient searching and backtracking without excessive overhead. The use of a set for results ensures that we avoid duplicates, and the visited set helps to manage the state during backtracking.    
9. Overall, this solution provides a robust and efficient way to find all valid words on the board based on the given list of words, leveraging the strengths of both trie data structures and backtracking algorithms. 
"""