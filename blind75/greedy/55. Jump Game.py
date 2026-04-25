#55. Jump Game
"""You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105"""

#answer
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
    
#example 1:
nums = [2,3,1,1,4]
solution = Solution()
print(solution.canJump(nums))  # Output: true
#example 2:
nums = [3,2,1,0,4]
solution = Solution()
print(solution.canJump(nums))  # Output: false
#example 3:
nums = [0]  
solution = Solution()
print(solution.canJump(nums))  # Output: true

"""walkthrough:
1. We initialize a variable `goal` to the last index of the array, which represents the target position we want to reach.           
2. We iterate through the array from the second-to-last index to the first index (in reverse order). For each index `i`, we check if we can jump from that index to the current `goal` index. This is done by checking if `i + nums[i] >= goal`. If this condition is true, it means we can jump from index `i` to the `goal` index or beyond.
3. If we can jump from index `i` to the `goal`, we update the `goal` to be index `i`, which means we now want to check if we can jump from an earlier index to index `i`.
4. After the loop, we check if `goal` is equal to 0. If it is, it means we can jump from the first index to the last index, and we return true. Otherwise, we return false. 
This approach effectively works backwards from the end of the array to determine if we can reach the last index starting from the first index."""