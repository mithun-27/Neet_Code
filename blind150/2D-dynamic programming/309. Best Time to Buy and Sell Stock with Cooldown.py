#309. Best Time to Buy and Sell Stock with Cooldown
"""You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Example 2:

Input: prices = [1]
Output: 0
 

Constraints:

1 <= prices.length <= 5000
0 <= prices[i] <= 1000"""

#answer:
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp1_buy, dp1_sell = 0, 0
        dp2_buy = 0

        for i in range(n - 1, -1, -1):
            dp_buy = max(dp1_sell - prices[i], dp1_buy)
            dp_sell = max(dp2_buy + prices[i], dp1_sell)
            dp2_buy = dp1_buy
            dp1_buy, dp1_sell = dp_buy, dp_sell

        return dp1_buy

#example:
"""Input
prices =
[1,2,3,0,2]
Output
3
Expected
3
"""


"""Walkthrough:
1. We want to maximize profit while buying and selling stocks multiple times. However, after selling a stock, we must wait one day before buying again due to the cooldown rule.
2. At any day, we can be in one of three states:
   - Holding a stock (`hold`)
   - Just sold a stock (`sell`)
   - Not holding a stock and free to buy (`cooldown/rest`)
3. Dynamic Programming is used because the best decision on the current day depends on the results of previous days.
4. The `hold` state represents the maximum profit achievable while currently owning a stock. We can either continue holding the previous stock or buy today from the cooldown/rest state.
5. The `sell` state represents the maximum profit achievable after selling a stock today. The only way to enter this state is by selling a stock that was previously held.
6. The `cooldown` (or rest) state represents the maximum profit when we are not holding a stock and are allowed to buy. We can either remain in cooldown or enter it after completing the cooldown day following a sale.
7. For each day's price, we update:
   - `hold = max(previous_hold, previous_cooldown - price)`
   - `sell = previous_hold + price`
   - `cooldown = max(previous_cooldown, previous_sell)`
8. These transitions ensure that:
   - We never buy immediately after selling.
   - We always consider the best possible profit for each state.
9. After processing all days, the answer is the maximum profit among the states where we are not holding a stock (`sell` or `cooldown`). The time complexity is `O(n)` because each price is processed once, and the auxiliary space complexity is `O(1)` since only a few variables are maintained."""