#53. Maximum Subarray
"""Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle."""


#answer:
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def dfs(l, r):
            if l > r:
                return float("-inf")

            m = (l + r) >> 1
            leftSum = rightSum = curSum = 0
            for i in range(m - 1, l - 1, -1):
                curSum += nums[i]
                leftSum = max(leftSum, curSum)

            curSum = 0
            for i in range(m + 1, r + 1):
                curSum += nums[i]
                rightSum = max(rightSum, curSum)

            return (max(dfs(l, m - 1),
                        dfs(m + 1, r),
                        leftSum + nums[m] + rightSum))

        return dfs(0, len(nums) - 1)

#example:
solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
print(solution.maxSubArray([1]))  # Output: 1
print(solution.maxSubArray([5,4,-1,7,8]))  # Output: 23


"""Walkthrough:
1. We want to find the maximum sum of any contiguous subarray in the given array `nums`.
2. This solution uses the Divide and Conquer approach, where the array is repeatedly divided into smaller halves.
3. For any range `[l, r]`, we calculate the middle index `m` and consider three possible locations for the maximum subarray:
   - Entirely in the left half.
   - Entirely in the right half.
   - Crossing the middle element.
4. The function `dfs(l, r)` returns the maximum subarray sum within the range `[l, r]`.
5. If `l > r`, the range is invalid, so we return negative infinity to ensure it is never chosen as the maximum.
6. To calculate the maximum subarray crossing the middle, we first find the largest possible sum extending from the middle toward the left side.
7. Similarly, we find the largest possible sum extending from the middle toward the right side.
8. The best crossing subarray must include the middle element, so its total sum is:
   `leftSum + nums[m] + rightSum`.
9. We recursively compute the maximum subarray sum in the left half and the right half.
10. The answer for the current range is the maximum among:
    - Maximum subarray entirely in the left half.
    - Maximum subarray entirely in the right half.
    - Maximum subarray crossing the middle.
11. By recursively solving smaller ranges and combining their results, we eventually obtain the maximum subarray sum for the entire array.
12. The time complexity is `O(n log n)` because each level of recursion processes all elements once while the recursion depth is `log n`, and the auxiliary space complexity is `O(log n)` due to the recursion stack."""