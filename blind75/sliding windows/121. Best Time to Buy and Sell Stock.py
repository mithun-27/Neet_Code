#121. Best Time to Buy and Sell Stock
"""You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104"""

#answer
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        mp=0
        while r < len(prices):
            if prices[l]<prices[r]:
                profit = prices[r]-prices[l]
                mp=max(mp,profit)
            else:
                l=r
            r+=1
        return mp
    
#example usage
solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))  # Output: 5
print(solution.maxProfit([7,6,4,3,1]))  # Output: 0
print(solution.maxProfit([1,2,3,4,5]))  # Output: 4

"""walkthrough the code:
1. We initialize two pointers, `l` and `r`, to represent the left and right indices of the prices array. We also initialize `mp` to store the maximum profit found so far.
2. We use a while loop to iterate through the prices array until the right pointer `r` reaches the end of the array.
3. Inside the loop, we check if the price at the left pointer `l` is less than the price at the right pointer `r`. If it is, we calculate the profit by subtracting the price at `l` from the price at `r` and update `mp` if this profit is greater than the current maximum profit.
4. If the price at `l` is not less than the price at `r`, we move the left pointer `l` to the right pointer `r`, effectively starting a new potential transaction from that point.  
5. We then move the right pointer `r` to the right to continue checking for potential profits.
6. Finally, we return the maximum profit found, which is stored in `mp`. If no profit can be made, `mp` will remain 0, which is the correct return value in that case.  
This algorithm runs in O(n) time complexity, where n is the length of the prices array, since we are traversing the array once with the two pointers. The space complexity is O(1) since we are using only a constant amount of extra space to store the pointers and the maximum profit.   
"""