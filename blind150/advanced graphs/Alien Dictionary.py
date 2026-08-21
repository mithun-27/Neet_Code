#Alien Dictionary
"""There is a new alien language that uses the English alphabet, but the order of the letters is unknown.

You are given a list of strings words from the alien language's dictionary. It is claimed that the strings in words are sorted lexicographically by the rules of this new language.

If this claim is incorrect, and the given arrangement of strings in words cannot correspond to any order of letters, return "".

Otherwise, return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there are multiple solutions, return any of them.

A string a is lexicographically smaller than a string b if either of the following is true:

The first letter where they differ is smaller in a than in b.
a is a prefix of b and a.length < b.length.

Example 1:

Input: words = ["z","o"]

Output: "zo"
Explanation:
From "z" and "o", we know 'z' < 'o', so return "zo".


Example 2:

Input: words = ["hrn","hrf","er","enn","rfnn"]

Output: "hernf"
Explanation:

from "hrn" and "hrf", we know 'n' < 'f'
from "hrf" and "er", we know 'h' < 'e'
from "er" and "enn", we know 'r' < 'n'
from "enn" and "rfnn" we know 'e' < 'r'
so one possible solution is "hernf"

Example 3:

Input: words = ["abc","ab"]

Output: ""
Explanation:
The second word is a prefix of the first word, but the first word appears before the second. This is impossible in a valid lexicographical ordering, so return "".


Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of only lowercase English letters."""


#answer :
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
"""Input:


words=["z","o"]
Your Output:


zo
Expected output:


zo"""

#example 2:
"""Input:


words=["hrn","hrf","er","enn","rfnn"]
Your Output:


hernf
Expected output:


hernf"""


"""Walkthrough:
1. We are given a list of words sorted according to the rules of an unknown language, and our goal is to determine the order of characters in that language.
2. We first create a graph where each unique character is a node. We also initialize an indegree count for every character, representing how many characters must come before it.
3. We compare each pair of adjacent words because the first position where they differ tells us the relative ordering of two characters.
4. For two consecutive words `w1` and `w2`, we find the first index where the characters are different. If `w1[j] != w2[j]`, then `w1[j]` must come before `w2[j]` in the foreign alphabet.
5. We add a directed edge from `w1[j]` to `w2[j]` and increase the indegree of `w2[j]`. We only add the edge once to avoid duplicate indegree counts.
6. Before processing character differences, we handle an invalid case: if `w1` is longer than `w2` and `w2` is a prefix of `w1`, then no valid character ordering exists, so we immediately return an empty string.
7. Once the graph is built, we perform Topological Sort using BFS (Kahn's Algorithm). We start by placing all characters with indegree `0` into a queue because they have no prerequisites.
8. We repeatedly remove a character from the queue, add it to the result, and decrease the indegree of its neighboring characters. Whenever a neighbor's indegree becomes `0`, we add it to the queue.
9. After the BFS finishes, if the result contains all characters, we join them into a string and return it as a valid character ordering. If some characters remain unprocessed, the graph contains a cycle, meaning no valid ordering exists, so we return an empty string. The time complexity is `O(C + E)`, where `C` is the number of unique characters and `E` is the number of ordering relationships, while the auxiliary space complexity is `O(C + E)` for the graph, indegree map, queue, and result."""