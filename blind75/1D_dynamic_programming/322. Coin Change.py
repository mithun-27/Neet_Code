#322. Coin Change
"""You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
 
"""

#answer
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        q = deque([0])
        seen = [False] * (amount + 1)
        seen[0] = True
        res = 0

        while q:
            res += 1
            for _ in range(len(q)):
                cur = q.popleft()
                for coin in coins:
                    nxt = cur + coin
                    if nxt == amount:
                        return res
                    if nxt > amount or seen[nxt]:
                        continue
                    seen[nxt] = True
                    q.append(nxt)

        return -1   
    
#example usage
solution = Solution()
print(solution.coinChange([1,2,5], 11)) # Output: 3
print(solution.coinChange([2], 3)) # Output: -1
print(solution.coinChange([1], 0)) # Output: 0

"""walkthrough
1. We start by checking if the amount is 0. If it is, we can return 0 immediately since no coins are needed.    
2. We initialize a queue (using deque) to perform a breadth-first search (BFS) and a seen list to keep track of the amounts we have already visited. We start by adding 0 to the queue and marking it as seen. We also initialize a variable res to keep track of the number of coins used.
3. We enter a while loop that continues until the queue is empty. Inside the loop, we increment res by 1 to account for the next level of BFS (which represents using one more coin).
4. We iterate through the current level of the queue (using a for loop) and for each amount (cur) we pop from the queue, we iterate through the list of coins. For each coin, we calculate the next amount (nxt) by adding the coin to the current amount.
5. If nxt is equal to the target amount, we return res since we have found the minimum number of coins needed. If nxt is greater than the target amount or has already been seen, we skip it. Otherwise, we mark nxt as seen and add it to the queue for further exploration.
6. If we exit the while loop without finding the target amount, we return -1 to indicate that it is not possible to make up the amount with the given coins.
7. The time complexity of this solution is O(amount * n), where n is the number of coins, since in the worst case we may need to explore all amounts up to the target amount for each coin. The space complexity is O(amount) due to the seen list and the queue.   
"""