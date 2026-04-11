#213. House Robber II
"""You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000"""

#answer
class Solution:

    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]),
                            self.helper(nums[:-1]))

    def helper(self, nums):
        rob1, rob2 = 0, 0

        for num in nums:
            newRob = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2
    
#example
solution = Solution()
print(solution.rob([2,3,2]))  # Output: 3
print(solution.rob([1,2,3,1]))  # Output: 4
print(solution.rob([1,2,3]))  # Output: 3   


"""walkthrough
1. Since the houses are arranged in a circle, we cannot rob both the first and the last house. Therefore, we have two scenarios to consider: robbing from the second house to the last house, or robbing from the first house to the second-to-last house.
2. We define a helper function `helper` that takes a list of house values and calculates the maximum amount of money that can be robbed using the same logic as in the House Robber problem (without the circular constraint).
3. In the main `rob` function, we return the maximum of three values: the amount from robbing the first house alone, the amount from robbing from the second house to the last house, and the amount from robbing from the first house to the second-to-last house.
4. The time complexity of this solution is O(n) since we are iterating through the list of houses twice (once for each scenario), and the space complexity is O(1) since we are using only a constant amount of space to store the variables in the helper function.
"""