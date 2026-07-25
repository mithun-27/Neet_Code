#46. Permutations
"""Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique."""

#answer
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack(nums, 0)
        return self.res

    def backtrack(self, nums: List[int], idx: int):
        if idx == len(nums):
            self.res.append(nums[:])
            return
        for i in range(idx, len(nums)):
            nums[idx], nums[i] = nums[i], nums[idx]
            self.backtrack(nums, idx + 1)
            nums[idx], nums[i] = nums[i], nums[idx]

#example 
"""Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
"""

"""Walkthrough:
1. We want to find all unique combinations of numbers from the `candidates` array whose sum is equal to the given `target`, where each number can be used only once.
2. We first sort the `candidates` array so that duplicate numbers are placed together. This allows us to easily skip duplicate combinations during the search.
3. We use a backtracking (depth-first search) approach to explore all possible combinations. At each recursive call, we iterate through the candidates starting from the current index.
4. For each candidate, we first check if it is a duplicate of the previous candidate at the same recursion level. If it is, we skip it to avoid generating duplicate combinations.
5. If the current candidate is greater than the remaining target, we stop exploring further because the array is sorted, and all remaining candidates will also be too large.
6. Otherwise, we include the current candidate in the current combination and recursively search for the remaining target. Since each element can be used only once, the next recursive call starts from the next index (`i + 1`).
7. If the remaining target becomes exactly `0`, we have found a valid combination, so we add a copy of the current combination to the result list.
8. After returning from the recursive call, we backtrack by removing the last added candidate and continue exploring the remaining candidates.
9. The algorithm continues until all possible unique combinations have been explored. The time complexity is exponential in the worst case because many combinations may need to be explored, while the auxiliary space complexity is `O(n)` for the recursion stack and the current combination (excluding the output list)."""