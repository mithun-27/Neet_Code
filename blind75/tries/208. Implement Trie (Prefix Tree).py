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
    
#example usage
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))   # return True 
print(trie.search("app"))     # return False
print(trie.startsWith("app")) # return True 
trie.insert("app")
print(trie.search("app"))     # return True
#output: True, False, True, True    

"""walkthrough the code:
1. The Trie class is initialized with an empty dictionary called root, which will serve as the starting point for our trie.     
2. The insert method takes a word as input and iterates through each letter in the word. For each letter, it checks if the letter is already a key in the current dictionary (cur). If not, it creates a new dictionary for that letter. Then it updates cur to point to the dictionary corresponding to that letter. After processing all letters, it adds a special key '*' to indicate the end of a word.    
3. The search method takes a word as input and iterates through each letter in the word, similar to the insert method. If at any point a letter is not found in the current dictionary, it returns False. If it successfully traverses through all letters, it checks if the '*' key is present in the final dictionary, which indicates that the word exists in the trie.    
4. The startsWith method is similar to the search method, but instead of checking for the '*' key at the end, it simply returns True if it successfully traverses through all letters of the prefix. If any letter is not found, it returns False.
5. The example usage demonstrates how to use the Trie class to insert words, search for words, and check for prefixes. The expected output is shown in the comments next to each operation.
"""