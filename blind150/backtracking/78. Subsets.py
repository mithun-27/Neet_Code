#78. Subsets
"""Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
 
"""

#answer
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        for i in range(1 << n):
            subset = [nums[j] for j in range(n) if (i & (1 << j))]
            res.append(subset)
        return res
    
#example 1:
solution = Solution()
nums = [1,2,3]
print(solution.subsets(nums)) #output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

#example 2:
nums = [0]
print(solution.subsets(nums)) #output: [[],[0]]

"""Walkthrough:
1. We want to generate all possible subsets (the power set) of the given array `nums`.
2. If the array contains `n` elements, there are exactly `2^n` possible subsets because each element has two choices: either include it or exclude it.
3. We loop from `0` to `(1 << n) - 1`, where each number represents one possible subset using its binary representation.
4. For each number `i`, we check every bit position `j`. If the `j`th bit is set (i.e., `i & (1 << j)` is non-zero), we include `nums[j]` in the current subset.
5. After checking all the bits, the constructed subset is added to the result list.
6. We repeat this process for every number from `0` to `2^n - 1`, ensuring that every possible combination of elements is generated exactly once.
7. The final result contains all subsets of the input array. The time complexity is `O(n × 2^n)` because we generate `2^n` subsets and examine all `n` elements for each subset. The auxiliary space complexity is `O(n)` (excluding the output), while the total space including the returned subsets is `O(n × 2^n)`."""