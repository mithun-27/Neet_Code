#1. Two Sum
"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists."""

#answer
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pm={}
        for i , n in enumerate(nums):
            diff=target - n
            if diff in pm:
                return [pm[diff],i]
            pm[n]=i

#example 1:
nums = [2,7,11,15]
target = 9
solution = Solution()
print(solution.twoSum(nums, target)) # Output: [0,1]

#example 2:
nums = [3,2,4]
target = 6
solution = Solution()
print(solution.twoSum(nums, target)) # Output: [1,2]

"""walkthrough:
1. We initialize an empty dictionary pm to store the numbers we have seen so far and their corresponding indices.
2. We iterate through the list of numbers using enumerate to get both the index i and the number n at that index.
3. For each number n, we calculate the difference diff between the target and n. This diff represents the number we need to find in order to reach the target.
4. We check if diff is already in the dictionary pm. If it is, it means we have found the two numbers that add up to the target, and we return their indices as a list [pm[diff], i].
5. If diff is not in the dictionary, we add the current number n and its index i to the dictionary pm for future reference.
6. The loop continues until we find the solution, which is guaranteed to exist according to the problem statement."""
