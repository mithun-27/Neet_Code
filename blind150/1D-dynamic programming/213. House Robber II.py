#213. House Robber II
"""You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000"""

#answer :
class Solution:

    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]),
                            self.helper(nums[:-1]))

    def helper(self, nums):
        rob1, rob2 = 0, 0

        for num in nums:
            newRob = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2

#example:
"""Input
nums =
[2,3,2]
Output
3
Expected
3
"""

#example:
"""Input
nums =
[1,2,3,1]
Output
4
Expected
4"""

#walkthrough:
"""Walkthrough:
1. This is the House Robber II problem, where the houses are arranged in a circle. Because the first and last houses are adjacent, we cannot rob both of them on the same night.
2. To handle the circular arrangement, we split the problem into two separate linear House Robber problems:
   - Rob houses from index `1` to `n-1` (exclude the first house).
   - Rob houses from index `0` to `n-2` (exclude the last house).
3. We also consider the special case where only the first house is robbed, which is represented by `nums[0]`.
4. The final answer is the maximum among:
   - `nums[0]`
   - Maximum profit from `nums[1:]`
   - Maximum profit from `nums[:-1]`
5. The `helper()` function solves the normal House Robber problem for a linear street using Dynamic Programming with constant space.
6. Inside `helper()`, `rob1` stores the maximum profit up to house `i-2`, and `rob2` stores the maximum profit up to house `i-1`.
7. For each house value `num`, we decide whether to rob it or skip it:
   - Rob it: `rob1 + num`
   - Skip it: `rob2`
   We choose the larger value using:
   `newRob = max(rob1 + num, rob2)`
8. After calculating `newRob`, we shift the DP window:
   - `rob1 = rob2`
   - `rob2 = newRob`
   This allows us to process the next house while keeping only the last two DP states.
9. After all houses have been processed, `rob2` contains the maximum profit for that linear arrangement. We compute the answer for both possible ranges and return the larger value. The time complexity is `O(n)` because each house is processed once, and the auxiliary space complexity is `O(1)` since only a few variables are used."""