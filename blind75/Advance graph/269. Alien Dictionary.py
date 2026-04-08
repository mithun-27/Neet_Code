#269. Alien Dictionary
"""There is a foreign language which uses the latin alphabet, but the order among letters is not "a", "b", "c" ... "z" as in English.

You receive a list of non-empty strings words from the dictionary, where the words are sorted lexicographically based on the rules of this new language.

Derive the order of letters in this language. If the order is invalid, return an empty string. If there are multiple valid order of letters, return any of them.

A string a is lexicographically smaller than a string b if either of the following is true:

The first letter where they differ is smaller in a than in b.
a is a prefix of b and a.length < b.length.
Example 1:

Input: ["z","o"]

Output: "zo"
Explanation:
From "z" and "o", we know 'z' < 'o', so return "zo".

Example 2:

Input: ["hrn","hrf","er","enn","rfnn"]

Output: "hernf"
Explanation:

from "hrn" and "hrf", we know 'n' < 'f'
from "hrf" and "er", we know 'h' < 'e'
from "er" and "enn", we know 'r' < 'n'
from "enn" and "rfnn" we know 'e' < 'r'
so one possible solution is "hernf"
Constraints:

The input words will contain characters only from lowercase 'a' to 'z'.
1 <= words.length <= 100
1 <= words[i].length <= 100"""

#answer
class Solution:
    def foreignDictionary(self, words):
        adj = {c: set() for w in words for c in w}
        indegree = {c: 0 for c in adj}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break

        q = deque([c for c in indegree if indegree[c] == 0])
        res = []

        while q:
            char = q.popleft()
            res.append(char)
            for neighbor in adj[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        if len(res) != len(indegree):
            return ""

        return "".join(res)
    
#example 1:
solution = Solution()
print(solution.foreignDictionary(["z","o"])) # Output: "zo"
print(solution.foreignDictionary(["hrn","hrf","er","enn","rfnn"])) # Output: "hernf"
print(solution.foreignDictionary(["abc","ab"])) # Output: ""

"""walkthrough the code:
1. We create an adjacency list `adj` to represent the graph of character dependencies and a dictionary `indegree` to count the number of incoming edges for each character.
2. We iterate through pairs of adjacent words in the input list to determine the order of characters. For each pair of words, we find the first position where they differ and add a directed edge from the character in the first word to the character in the second word. We also update the indegree of the second character. If the first word is longer than the second word and they are identical up to the length of the second word, we return an empty string since the order is invalid.
3. We perform a topological sort using a queue to process characters with zero indegree.
4. We append characters to the result list as we process them and decrease the indegree of their neighbors. If any neighbor's indegree becomes zero, we add it to the queue.
5. Finally, if the length of the result list is not equal to the number of unique characters, it means there is a cycle in the graph, and we return an empty string. Otherwise, we join the characters in the result list to form the final order of characters and return it.      
6. The time complexity of this solution is O(C + N) where C is the total number of characters in all words and N is the number of unique characters. The space complexity is O(C + N) for the adjacency list and indegree dictionary.   
"""