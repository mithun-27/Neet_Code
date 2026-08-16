#127. Word Ladder
"""A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

Constraints:

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique."""

#answer:
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0
        m = len(wordList[0])
        wordSet = set(wordList)
        qb, qe = deque([beginWord]), deque([endWord])
        fromBegin, fromEnd = {beginWord: 1}, {endWord: 1}

        while qb and qe:
            if len(qb) > len(qe):
                qb, qe = qe, qb
                fromBegin, fromEnd = fromEnd, fromBegin
            for _ in range(len(qb)):
                word = qb.popleft()
                steps = fromBegin[word]
                for i in range(m):
                    for c in range(97, 123):
                        if chr(c) == word[i]:
                            continue
                        nei = word[:i] + chr(c) + word[i + 1:]
                        if nei not in wordSet:
                            continue
                        if nei in fromEnd:
                            return steps + fromEnd[nei]
                        if nei not in fromBegin:
                            fromBegin[nei] = steps + 1
                            qb.append(nei)
        return 0

#example 1 :
"""Input
beginWord =
"hit"
endWord =
"cog"
wordList =
["hot","dot","dog","lot","log","cog"]
Output
5
Expected
5
"""

#example 2 :
"""Input
beginWord =
"hit"
endWord =
"cog"
wordList =
["hot","dot","dog","lot","log"]
Output
0
Expected
0"""

"""Walkthrough:
1. We want to find the length of the shortest transformation sequence from `beginWord` to `endWord`, where only one letter can be changed at a time and every intermediate word must exist in `wordList`.
2. Since we need the shortest sequence, we use Breadth-First Search (BFS). BFS explores words level by level, guaranteeing that the first time we reach `endWord` is through the shortest path.
3. To efficiently find neighboring words, we create a mapping of generic patterns to words. For example, the word `"hot"` generates the patterns `"*ot"`, `"h*t"`, and `"ho*"`. All words sharing the same pattern differ by only one letter and are potential transformations.
4. We preprocess every word in `wordList` and store them in a dictionary where each pattern points to all words that match that pattern.
5. We initialize a BFS queue with `beginWord` and start the transformation length as `1` because the sequence already contains the starting word.
6. During BFS, we remove a word from the queue and generate all of its generic patterns. For each pattern, we retrieve all neighboring words that differ by exactly one character.
7. If any neighboring word is equal to `endWord`, we return the current transformation length plus one because we have found the shortest valid sequence.
8. Otherwise, every unvisited neighboring word is added to the queue and marked as visited so that it is processed only once. This prevents cycles and unnecessary repeated work.
9. If the queue becomes empty without reaching `endWord`, no valid transformation sequence exists, so we return `0`. The time complexity is approximately `O(N × L²)`, where `N` is the number of words and `L` is the word length, while the auxiliary space complexity is `O(N × L)` for the pattern mapping, visited set, and BFS queue."""