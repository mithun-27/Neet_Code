#763. Partition Labels
"""You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

 

Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
Example 2:

Input: s = "eccbbbbdec"
Output: [10]
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters."""


#answer:
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i

        res = []
        size = end = 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])

            if i == end:
                res.append(size)
                size = 0
        return res


#example:
"""Input
s =
"ababcbacadefegdehijhklij"
Output
[9,7,8]
Expected
[9,7,8]"""

#example:
"""Input
s =
"eccbbbbdec"
Output
[10]
Expected
[10]
"""


"""Walkthrough:
1. We want to divide the string into as many partitions as possible such that each character appears in at most one partition.
2. To determine where a partition can end, we first need to know the last occurrence of every character in the string.
3. We traverse the string once and store the final index of each character in a dictionary called `lastIndex`.
4. After building this dictionary, we scan the string again from left to right to construct the partitions.
5. We maintain two variables: `end`, which represents the farthest index the current partition must reach, and `size`, which tracks the current partition length.
6. For every character at index `i`, we increase the partition size by one because the character belongs to the current partition.
7. We update `end` using the last occurrence of the current character:
   `end = max(end, lastIndex[c])`.
8. This ensures that the current partition includes all future occurrences of every character seen so far.
9. As we continue scanning, the partition boundary may extend whenever we encounter a character whose last occurrence is farther to the right.
10. We keep expanding the partition until the current index `i` reaches the value of `end`.
11. When `i == end`, it means all characters within the current partition have their last occurrences inside this range.
12. Therefore, no character from the current partition will appear later in the string, making it a valid partition boundary.
13. We add the current partition size to the result list and reset `size` to begin tracking the next partition.
14. The process repeats until every character in the string has been processed.
15. By always extending the partition to the farthest last occurrence of any character seen so far, we guarantee that characters do not appear in multiple partitions.
16. This greedy strategy also produces the maximum possible number of valid partitions.
17. After the traversal is complete, the result list contains the sizes of all partitions.
18. The time complexity is `O(n)` because the string is traversed twice, and the auxiliary space complexity is `O(k)` where `k` is the number of distinct characters stored in the dictionary."""