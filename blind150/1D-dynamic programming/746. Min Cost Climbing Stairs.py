#746. Min Cost Climbing Stairs
"""You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
 

Constraints:

2 <= cost.length <= 1000
0 <= cost[i] <= 999"""

#answer :
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])


#example:
"""Input
cost =
[10,15,20]
Output
15
Expected
15"""


#walkthrough:
"""Walkthrough:
1. We want to find the minimum cost required to reach the top of the staircase. From any stair, we can climb either 1 step or 2 steps at a time.
2. Instead of calculating the minimum cost from the beginning, we work backwards from the end of the `cost` array using Dynamic Programming.
3. The key idea is that the minimum cost to start from stair `i` equals the cost of the current stair plus the cheaper of the two possible next moves: stair `i+1` or stair `i+2`.
4. We iterate from the third-last stair toward the first stair because the last two stairs already represent their own minimum costs.
5. For each stair `i`, we update:
   `cost[i] = cost[i] + min(cost[i+1], cost[i+2])`
   This stores the minimum total cost required to reach the top when starting from stair `i`.
6. As the loop progresses, each position in the array is transformed from its original cost into the minimum cost needed to reach the top from that position.
7. After processing all stairs, `cost[0]` represents the minimum cost if we start from stair `0`, and `cost[1]` represents the minimum cost if we start from stair `1`.
8. Since we are allowed to start from either stair `0` or stair `1`, the answer is the smaller of these two values.
9. The algorithm returns `min(cost[0], cost[1])`. The time complexity is `O(n)` because each stair is processed exactly once, and the auxiliary space complexity is `O(1)` since the input array itself is used to store the dynamic programming results."""