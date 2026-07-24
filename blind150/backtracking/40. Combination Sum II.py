#40. Combination Sum II
"""Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30"""

#answer
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(idx, path, cur):
            if cur == target:
                res.append(path.copy())
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if cur + candidates[i] > target:
                    break

                path.append(candidates[i])
                dfs(i + 1, path, cur + candidates[i])
                path.pop()

        dfs(0, [], 0)
        return res

#example
"""Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 """

"""Walkthrough:
1. We want to find all unique combinations of numbers from the `candidates` array whose sum is equal to the given `target`, where each number can be used at most once.
2. We first sort the `candidates` array so that duplicate values are placed next to each other. This makes it easy to skip duplicate combinations during the search.
3. We use a backtracking (depth-first search) approach to explore all possible combinations. At each recursive call, we iterate through the remaining candidates starting from the current index.
4. For each candidate, we decide whether to include it in the current combination. Since each number can only be used once, the next recursive call starts from the next index (`i + 1`).
5. If the remaining target becomes exactly `0`, we have found a valid combination, so we add a copy of the current combination to the result list.
6. If the remaining target becomes negative or we reach the end of the array, we stop exploring that path because it cannot produce a valid solution.
7. To avoid duplicate combinations, if the current candidate is the same as the previous candidate at the same recursion level, we skip it. This ensures that combinations like `[1,2,5]` are generated only once.
8. After exploring a candidate, we backtrack by removing it from the current combination and continue checking the remaining candidates. This allows us to explore every unique valid combination without repetition.
9. The algorithm continues until all possible combinations have been explored. The time complexity is exponential in the worst case because all valid combinations may need to be examined, while the auxiliary space complexity is `O(n)` for the recursion stack and the current combination (excluding the output list)."""