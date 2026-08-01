#208. Implement Trie (Prefix Tree)
"""A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
 

Constraints:

1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith."""

#answer
class Trie:

    def __init__(self):
        self.root={}
        
    def insert(self, word: str) -> None:

        cur=self.root

        for letter in word:
            if letter not in cur:
                cur[letter]={}
            cur=cur[letter]

        cur['*']=''

    def search(self, word: str) -> bool:

        cur=self.root
        for letter in word:
            if letter not in cur:
                return False
            cur=cur[letter]

        return '*' in cur
        
    def startsWith(self, prefix: str) -> bool:

        cur=self.root
        for letter in prefix:
            if letter not in cur:
                return False
            cur=cur[letter]

        return True

#example:
"""Input:
["Trie", "insert", "dog", "search", "dog", "search", "do", "startsWith", "do", "insert", "do", "search", "do"]

Output:
[null, null, true, false, true, null, true]

Explanation:
PrefixTree prefixTree = new PrefixTree();
prefixTree.insert("dog");
prefixTree.search("dog");    // return true
prefixTree.search("do");     // return false
prefixTree.startsWith("do"); // return true
prefixTree.insert("do");
prefixTree.search("do");     // return true"""


"""Walkthrough:
1. We want to design a Trie (Prefix Tree) that efficiently stores words and supports three operations: inserting a word, searching for a complete word, and checking whether any stored word starts with a given prefix.
2. Each Trie node stores a collection of child nodes (one for each possible character) and a boolean flag indicating whether the current node represents the end of a valid word.
3. During the `insert()` operation, we start from the root node and process each character of the word one by one. If a child node for the current character does not exist, we create it. We then move to that child node and continue until all characters have been inserted.
4. After inserting the last character, we mark the current node as the end of a word. This distinguishes complete words from prefixes.
5. During the `search()` operation, we again start from the root node and follow the path corresponding to each character of the given word. If any character is missing, the word does not exist, so we return `False`.
6. After processing all characters, we return `True` only if the current node is marked as the end of a word. Otherwise, the characters represent only a prefix, not a complete word.
7. During the `startsWith()` operation, we follow the same traversal as `search()`. If every character of the prefix exists in the Trie, we return `True` regardless of whether the final node is marked as the end of a word.
8. Since each operation processes one character at a time without scanning the entire Trie, insertion, searching, and prefix checking are all performed efficiently.
9. Let `L` be the length of the input word or prefix. The time complexity of `insert()`, `search()`, and `startsWith()` is `O(L)` because each character is processed exactly once. The auxiliary space complexity for each operation is `O(1)` (excluding the space required to store the Trie), while inserting a new word may require up to `O(L)` additional space for newly created nodes."""