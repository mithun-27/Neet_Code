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
            for a in range(1, amount + 1):
                dp[a] += dp[a - coins[i]] if coins[i] <= a else 0
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
4"""


#example:
"""Input
amount =
3
coins =
[2]
Output
0
Expected
0"""

#example:
"""Input
amount =
10
coins =
[10]
Output
1
Expected
1
"""

"""Walkthrough:
1. We want to find the number of unique combinations of coins that can make up the given `amount`, where each coin can be used an unlimited number of times.
2. This is a Dynamic Programming problem where we count combinations rather than minimizing or maximizing a value.
3. We create a DP array `dp` of size `amount + 1`, where `dp[a]` represents the number of ways to form amount `a`.
4. The base case is `dp[0] = 1` because there is exactly one way to form amount `0` — by choosing no coins.
5. We process the coins one by one. For each coin, we update all amounts from `1` to `amount`.
6. For a particular amount `a`, if the current coin value is less than or equal to `a`, then any way to form `a - coin` can be extended by adding the current coin to form `a`.
7. Therefore, we update:
   ```python
   dp[a] += dp[a - coin]"""