#494. Target Sum
"""You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

 

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:

Input: nums = [1], target = 1
Output: 1
 

Constraints:

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000"""

#answer:
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for num in nums:
            next_dp = defaultdict(int)
            for total, count in dp.items():
                next_dp[total + num] += count
                next_dp[total - num] += count
            dp = next_dp

        return dp[target]


#example:
"""Input
nums =
[1,1,1,1,1]
target =
3
Output
5
Expected
5"""

"""Walkthrough:
1. We want to find the number of ways to assign either a `'+'` or `'-'` sign to each number in `nums` so that the final expression evaluates to the given `target`.
2. This is a Dynamic Programming problem where we track all possible sums that can be formed after processing each number.
3. We use a hash map (`dp`) where:
   `dp[sum] = number of ways to achieve that sum`.
4. Initially, before processing any numbers, we have:
   `dp[0] = 1`
   because there is exactly one way to obtain a sum of `0` — by choosing no numbers.
5. We process the numbers one by one. For each number `num`, we create a new hash map called `next_dp`.
6. For every existing sum `total` in `dp`, we have two choices:
   - Add the current number: `total + num`
   - Subtract the current number: `total - num`
7. If there are `count` ways to reach `total`, then:
   - `count` ways contribute to `total + num`
   - `count` ways contribute to `total - num`
   Therefore:
   `next_dp[total + num] += count`
   `next_dp[total - num] += count`
8. After processing all existing sums, `next_dp` contains every possible sum and the number of ways to achieve it after including the current number. We then replace `dp` with `next_dp`.
9. Once all numbers have been processed, `dp[target]` contains the total number of valid expressions that evaluate to the target value. The time complexity is `O(n × S)`, where `S` is the number of distinct sums generated during the process, and the auxiliary space complexity is also `O(S)` for the hash maps."""