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
    
#example usage
solution = Solution()
result = solution.combinationSum([2,3,6,7], 7)
print(result)

"""walkthrough
1. Sort the input array to ensure that we can stop early when the sum exceeds the target.
2. Define a recursive function dfs that takes the current index, the current combination being built, and the current total sum of that combination.
3. If the total equals the target, we add a copy of the current combination to the result list and return.
4. Iterate through the candidates starting from the current index:
   a. If adding the current candidate exceeds the target, we can break out of the loop since all subsequent candidates will also exceed the target.
   b. Otherwise, we add the current candidate to the current combination and recursively call dfs with the same index (since we can reuse the same candidate) and the updated total.
   c. After exploring that path, we remove the last candidate from the current combination (backtrack) and continue to the next candidate.
5. Finally, we call dfs starting from index 0 with an empty combination and a total of 0, and return the result list.   
This approach efficiently explores all possible combinations of candidates while ensuring that we do not exceed the target sum, and it handles duplicates by only allowing combinations to be built in a non-decreasing order."""