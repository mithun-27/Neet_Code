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
0 <= prices[i] <= 1000
 
"""


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
3"""

#example:
"""Input
prices =
[1]
Output
0
Expected
0
"""

"""Walkthrough:
1. We want to find the maximum profit that can be earned by buying and selling stocks any number of times, with the restriction that after selling a stock, we must wait one day before buying again (cooldown period).
2. At every day, we can be in one of two main states:
   - Buy state: we are allowed to buy a stock.
   - Sell state: we currently hold a stock and can choose to sell it.
3. Let:
   - `buy[i]` = maximum profit starting from day `i` when we are allowed to buy.
   - `sell[i]` = maximum profit starting from day `i` when we currently hold a stock.
4. Instead of storing full DP arrays, this solution keeps only the future values that are needed, reducing the space complexity to `O(1)`.
5. We process the prices from right to left because each state depends on future days.
6. When we are in the buy state on day `i`, we have two choices:
   - Buy the stock today and move to the sell state:
     `sell[i+1] - prices[i]`
   - Skip today and remain in the buy state:
     `buy[i+1]`
   Therefore:
   ```python
   buy[i] = max(sell[i+1] - prices[i], buy[i+1])"""