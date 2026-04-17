#152. Maximum Product Subarray
"""Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Note that the product of an array with a single element is the value of that element.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any subarray of nums is guaranteed to fit in a 32-bit integer."""

#answer
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n, res = len(nums), nums[0]
        prefix = suffix = 0

        for i in range(n):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[n - 1 - i] * (suffix or 1)
            res = max(res, max(prefix, suffix))
        return res

#example
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

"""walkthrough:
1. We initialize the variables `prefix` and `suffix` to 0, and `res` to the first element of the array.
2. We iterate through the array from both ends simultaneously using a loop that runs `n` times, where `n` is the length of the array.
3. In each iteration, we update `prefix` by multiplying it with the current element from the left side of the array. If `prefix` is 0, we use 1 instead to avoid resetting the product.
4. Similarly, we update `suffix` by multiplying it with the current element from the right side of the array. If `suffix` is 0, we use 1 instead to avoid resetting the product.
5. We then update `res` to be the maximum of the current `res`, `prefix`, and `suffix`.
6. After the loop, we return `res`, which contains the maximum product of any subarray in the input array.
This approach works because it considers both the products of subarrays starting from the left and the right, which allows it to handle cases where negative numbers can flip the sign of the product. By keeping track of both `prefix` and `suffix`, we can ensure that we capture the maximum product even when there are negative numbers in the array."""