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
-104 <= nums[i] <= 104"""

#answer
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
    
#example 1:
nums = [-2,1,-3,4,-1,2,1,-5,4]
solution = Solution()
print(solution.maxSubArray(nums))  # Output: 6
#example 2:
nums = [1]
solution = Solution()
print(solution.maxSubArray(nums))  # Output: 1
#example 3:
nums = [5,4,-1,7,8]
solution = Solution()
print(solution.maxSubArray(nums))  # Output: 23 

"""walkthrough:
1. The function `maxSubArray` takes a list of integers `nums` as input and defines a nested function `dfs` that performs a divide-and-conquer approach to find the maximum subarray sum.
2. The `dfs` function takes two parameters, `l` and `r`, which represent the left and right indices of the current subarray being evaluated.
3. If `l` is greater than `r`, it means we have an invalid subarray, and we return negative infinity to indicate that this subarray cannot contribute to the maximum sum.
4. We calculate the middle index `m` of the current subarray.   
5. We initialize `leftSum`, `rightSum`, and `curSum` to 0. We then iterate from the middle index `m - 1` down to `l`, adding each element to `curSum` and updating `leftSum` to be the maximum of itself and `curSum`. This loop calculates the maximum sum of a subarray that ends at index `m`.
6. We reset `curSum` to 0 and iterate from the middle index `m + 1` up to `r`, adding each element to `curSum` and updating `rightSum` to be the maximum of itself and `curSum`. This loop calculates the maximum sum of a subarray that starts at index `m`.
7. Finally, we return the maximum of three values: the result of recursively calling `dfs` on the left half of the subarray, the result of recursively calling `dfs` on the right half of the subarray, and the sum of `leftSum`, the middle element `nums[m]`, and `rightSum`. This ensures that we consider all possible subarrays that could yield the maximum sum.
8. The initial call to `dfs` is made with the indices of the entire array, and the final result is returned as the output of `maxSubArray`. 
This approach effectively breaks down the problem into smaller subproblems, allowing us to find the maximum subarray sum in a more efficient manner than a brute-force approach. The time complexity of this solution is O(n log n) due to the divide-and-conquer strategy."""