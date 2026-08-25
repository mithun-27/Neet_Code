#198. House Robber
"""You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400"""

#answer :
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for num in nums:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2


#example:
"""Input
nums =
[1,2,3,1]
Output
4
Expected
4
"""


#walkthrough:
"""Walkthrough:
1. We want to maximize the amount of money robbed from the houses without robbing two adjacent houses, because robbing adjacent houses would trigger the alarm.
2. At each house, we have two choices: either rob the current house or skip it.
3. If we rob the current house, we cannot rob the previous house, so the total money becomes:
   `current_house_money + profit_until_house_(i-2)`.
4. If we skip the current house, the total money remains:
   `profit_until_house_(i-1)`.
5. Therefore, the recurrence relation is:
   `dp[i] = max(dp[i-1], nums[i] + dp[i-2])`.
6. Instead of storing the entire DP array, we only keep track of the last two computed values because each state depends only on the previous two states.
7. Let:
   - `rob1` = maximum profit up to house `i-2`
   - `rob2` = maximum profit up to house `i-1`
8. For each house amount `n`, we calculate:
   `newRob = max(rob2, rob1 + n)`
   This chooses the better option between skipping the current house or robbing it.
9. We update `rob1 = rob2` and `rob2 = newRob` and continue until all houses are processed. The final answer is stored in `rob2`. The time complexity is `O(n)` because each house is processed once, and the auxiliary space complexity is `O(1)` since only two variables are used."""