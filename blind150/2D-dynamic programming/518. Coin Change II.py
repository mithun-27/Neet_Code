#518. Coin Change II
"""You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The final answer is guaranteed to fit into a signed 32-bit integer.

 

Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1
 

Constraints:

1 <= coins.length <= 300
1 <= coins[i] <= 5000
All the values of coins are unique.
0 <= amount <= 5000"""

#answer:
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins) - 1, -1, -1):
            nextDP = [0] * (amount + 1)
            nextDP[0] = 1

            for a in range(1, amount + 1):
                nextDP[a] = dp[a]
                if a - coins[i] >= 0:
                    nextDP[a] += nextDP[a - coins[i]]
            dp = nextDP
        return dp[amount]


#example:
"""Input
amount =
5
coins =
[1,2,5]
Output
4
Expected
4
"""


"""Walkthrough:
1. We want to find the number of different combinations of coins that can make up the given `amount`. Each coin can be used an unlimited number of times.
2. This is a Dynamic Programming problem where we count combinations rather than finding a minimum or maximum value.
3. We create a DP array where:
   `dp[a]` = number of ways to make amount `a` using the coins processed so far.
4. The base case is:
   `dp[0] = 1`
   because there is exactly one way to make amount `0` — by choosing no coins.
5. We process the coins one by one from right to left. For each coin, we build a new DP array called `nextDP`.
6. For every amount `a`, we first copy:
   `nextDP[a] = dp[a]`
   This represents all combinations that do not use the current coin.
7. If the current coin can fit into the amount (`a - coins[i] >= 0`), we add:
   `nextDP[a] += nextDP[a - coins[i]]`
   This represents combinations that use the current coin at least once.
8. Notice that we use `nextDP[a - coins[i]]` rather than `dp[a - coins[i]]`. This allows the same coin to be used multiple times because the current row's results are immediately available.
9. After processing all amounts for the current coin, we replace `dp` with `nextDP`. When all coins have been processed, `dp[amount]` contains the total number of unique combinations. The time complexity is `O(n × amount)`, where `n` is the number of coins, and the auxiliary space complexity is `O(amount)`."""