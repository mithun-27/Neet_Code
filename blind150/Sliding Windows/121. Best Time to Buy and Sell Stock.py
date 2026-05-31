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
    
#example 1:
prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices)) # Output: 5
#example 2:
prices = [7,6,4,3,1]
print(Solution().maxProfit(prices)) # Output: 0
#example 3:
prices = [1,2,3,4,5]
print(Solution().maxProfit(prices)) # Output: 4

"""walkthrough:
1. We initialize two pointers, l and r, to the first and second elements of the prices array, respectively. We also initialize a variable mp to store the maximum profit.
2. We enter a while loop that continues until the right pointer reaches the end of the prices array.
3. Inside the loop, we compare the prices at the left and right pointers. If the price at the left pointer is less than the price at the right pointer, it means we can make a profit by buying at the left pointer and selling at the right pointer. We calculate this profit and update mp if it's greater than the current maximum profit.   
4. If the price at the left pointer is greater than or equal to the price at the right pointer, it means we cannot make a profit by selling at the right pointer. In this case, we move the left pointer to the right pointer, effectively starting a new potential transaction from that point.    
5. We then move the right pointer to the next position and repeat the process until we have checked all possible transactions.  
6. Finally, we return mp, which contains the maximum profit that can be achieved from a single transaction.
7. The time complexity of this algorithm is O(n) since we traverse the prices array at most once, and the space complexity is O(1) as we only use a constant amount of extra space.
8. This approach efficiently calculates the maximum profit without needing to check every possible pair of days, which would have a time complexity of O(n^2).    """