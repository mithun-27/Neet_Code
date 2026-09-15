#312. Burst Balloons
"""You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

 

Example 1:

Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
Example 2:

Input: nums = [1,5]
Output: 10
 

Constraints:

n == nums.length
1 <= n <= 300
0 <= nums[i] <= 100"""


#answer:
class Solution:
    def maxCoins(self, nums):
        n = len(nums)
        new_nums = [1] + nums + [1]

        dp = [[0] * (n + 2) for _ in range(n + 2)]
        for l in range(n, 0, -1):
            for r in range(l, n + 1):
                for i in range(l, r + 1):
                    coins = new_nums[l - 1] * new_nums[i] * new_nums[r + 1]
                    coins += dp[l][i - 1] + dp[i + 1][r]
                    dp[l][r] = max(dp[l][r], coins)

        return dp[1][n]


#example:
"""Input
nums =
[3,1,5,8]
Output
167
Expected
167"""


"""Walkthrough:
1. We want to maximize the number of coins obtained by bursting all balloons, where bursting a balloon gives `left * current * right` coins based on its current neighbors.
2. Since the neighbors of a balloon change whenever other balloons are burst, it is difficult to decide which balloon to burst first.
3. To simplify the problem, we think in reverse and choose the **last balloon to burst** within a range instead of the first.
4. We add virtual balloons with value `1` at both ends of the array so that every balloon always has valid left and right neighbors.
5. We define `dp[l][r]` as the maximum coins that can be collected by bursting all balloons between indices `l` and `r` inclusive.
6. For every interval `[l, r]`, we try each balloon `i` as the last balloon to burst in that interval.
7. If `i` is burst last, then all balloons on its left and right inside the interval have already been removed, so its neighbors become `new_nums[l-1]` and `new_nums[r+1]`.
8. The coins earned in this case are `new_nums[l-1] * new_nums[i] * new_nums[r+1]` plus the best results from the left subinterval `dp[l][i-1]` and the right subinterval `dp[i+1][r]`.
9. We compute this value for every possible last balloon `i` and store the maximum value in `dp[l][r]`.
10. The intervals are processed from smaller ranges to larger ranges so that all required subproblems are already solved before being used.
11. After filling the DP table, `dp[1][n]` contains the maximum coins obtainable by bursting all balloons.
12. The time complexity is `O(n³)` because for every interval we try every possible last balloon, and the auxiliary space complexity is `O(n²)` for the DP table."""