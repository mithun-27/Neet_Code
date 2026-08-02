#211. Design Add and Search Words Data Structure
"""Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

Constraints:

1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 2 dots in word for search queries.
At most 104 calls will be made to addWord and search."""

#answer:
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()      

    def addWord(self, word):
        current_node = self.root
        for character in word:
            current_node = current_node.children.setdefault(character, TrieNode())
        current_node.is_word = True
        
    def search(self, word):
        def dfs(node, index):
            if index == len(word):
                return node.is_word
               
            if word[index] == ".":
                for child in node.children.values():
                    if dfs(child, index+1):
                        return True
                    
            if word[index] in node.children:
                return dfs(node.children[word[index]], index+1)
            
            return False
    
        return dfs(self.root, 0)

#example 1:
"""Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]
Expected
[null,null,null,null,false,true,true,true]"""


"""Walkthrough:
1. We want to design a data structure that supports adding words and searching for words, where the search pattern may contain the wildcard character `'.'`, which can match any single lowercase letter.
2. We use a Trie (Prefix Tree) to store all the words. Each Trie node contains a collection of child nodes and a boolean flag indicating whether the current node represents the end of a valid word.
3. During the `addWord()` operation, we start from the root node and process each character of the word one by one. If a child node for the current character does not exist, we create it and move to that child node.
4. After inserting the last character, we mark the current node as the end of a word. This allows us to distinguish complete words from prefixes.
5. During the `search()` operation, we perform a depth-first search (DFS) on the Trie. We examine one character of the search pattern at a time while traversing the Trie.
6. If the current character is a lowercase letter, we simply move to the corresponding child node. If the child does not exist, we return `False` because no matching word is possible.
7. If the current character is `'.'`, it can represent any letter. Therefore, we recursively search every child node of the current Trie node. If any recursive call returns `True`, the search is successful.
8. When all characters in the search pattern have been processed, we return `True` only if the current Trie node is marked as the end of a valid word. Otherwise, we return `False`.
9. Let `L` be the length of the search word. The time complexity of `addWord()` is `O(L)`. The time complexity of `search()` is `O(L)` when there are no wildcards, but in the worst case it becomes exponential because `'.'` may branch into multiple recursive searches. The auxiliary space complexity is `O(L)` for the recursion stack during the search (excluding the space required to store the Trie)."""