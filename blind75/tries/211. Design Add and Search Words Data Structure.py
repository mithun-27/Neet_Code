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

#answer
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
    
#example usage
wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
print(wordDictionary.search("pad")) # return False
print(wordDictionary.search("bad")) # return True
print(wordDictionary.search(".ad")) # return True
print(wordDictionary.search("b..")) # return True

"""walkthrough the code:
1. We define a TrieNode class to represent each node in the trie. Each node has a dictionary of children and a boolean flag to indicate if it represents the end of a word.
2. The WordDictionary class initializes with a root TrieNode.
3. The addWord method iterates through each character in the word, creating new TrieNodes as needed. After processing all characters, it marks the last node as a word.
4. The search method uses a depth-first search (DFS) approach to handle the search query. It checks if the current index has reached the end of the word, in which case it returns whether the current node is a word. If the current character is a dot, it recursively checks all children nodes. If the character is a specific letter, it checks if that letter exists in the children and continues the search. If neither condition is met, it returns False. This allows for efficient searching even with the presence of wildcard characters (dots).       
5. The example usage demonstrates how to add words to the WordDictionary and search for both exact matches and patterns with dots. The expected output is shown in the comments.        
"""