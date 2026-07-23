#39. Combination Sum
"""Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
 

Constraints:

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40"""

#answer
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                cur.append(nums[j])
                dfs(j, cur, total + nums[j])
                cur.pop()

        dfs(0, [], 0)
        return res

"""Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []"""

"""Walkthrough:
1. We want to find all unique combinations of numbers from the `candidates` array whose sum is equal to the given `target`.
2. Since each candidate can be used an unlimited number of times, we use a backtracking (depth-first search) approach to explore every possible combination.
3. At each recursive call, we decide whether to include the current candidate in the combination. If we include it, we subtract its value from the remaining target and continue from the same index so that the candidate can be reused.
4. If the remaining target becomes exactly `0`, we have found a valid combination, so we add a copy of the current combination to the result list.
5. If the remaining target becomes negative or we have considered all candidates, we stop exploring that path because it cannot produce a valid solution.
6. After exploring a candidate, we backtrack by removing it from the current combination and continue exploring the next candidates. This ensures that every possible valid combination is considered without modifying previously found solutions.
7. Since we always move forward through the candidate list (or stay at the same index when reusing a number), duplicate combinations such as `[2,3,2]` and `[3,2,2]` are avoided automatically.
8. The algorithm continues until all possible combinations have been explored. The time complexity is exponential in the worst case because many combinations may need to be explored, while the space complexity is `O(target)` for the recursion stack and the current combination (excluding the output list)."""