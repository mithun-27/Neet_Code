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


#answer:
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n, res = len(nums), nums[0]
        prefix = suffix = 0

        for i in range(n):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[n - 1 - i] * (suffix or 1)
            res = max(res, max(prefix, suffix))
        return res

#example:
"""Input
nums =
[2,3,-2,4]
Output
6
Expected
6"""

"""Walkthrough:
1. We want to find the maximum product of a contiguous subarray within the given array.
2. Unlike the Maximum Subarray Sum problem, products are tricky because multiplying by a negative number can turn a very small value into a very large value and vice versa.
3. Instead of explicitly tracking maximum and minimum products, this solution uses both a prefix product and a suffix product to handle negative numbers and zeros efficiently.
4. We initialize:
   - `res` as the first element, which stores the maximum product found so far.
   - `prefix` as `0`, representing the product from left to right.
   - `suffix` as `0`, representing the product from right to left.
5. We iterate through the array once. At each step:
   - `prefix = nums[i] * (prefix or 1)`
   - `suffix = nums[n-1-i] * (suffix or 1)`
   The expression `(prefix or 1)` resets the product to `1` whenever the previous product becomes `0`.
6. The prefix scan computes the product of subarrays from left to right, while the suffix scan computes the product from right to left.
7. Scanning in both directions is important because a maximum product subarray may start after a negative number or end before a negative number. One of the two scans will capture the optimal product.
8. After updating the prefix and suffix products, we compare both with the current answer and update:
   `res = max(res, prefix, suffix)`
9. Once the traversal is complete, `res` contains the largest product of any contiguous subarray. The time complexity is `O(n)` because the array is scanned once, and the auxiliary space complexity is `O(1)` since only a few variables are used.Walkthrough:
1. We want to find the maximum product of a contiguous subarray within the given array.
2. Unlike the Maximum Subarray Sum problem, products are tricky because multiplying by a negative number can turn a very small value into a very large value and vice versa.
3. Instead of explicitly tracking maximum and minimum products, this solution uses both a prefix product and a suffix product to handle negative numbers and zeros efficiently.
4. We initialize:
   - `res` as the first element, which stores the maximum product found so far.
   - `prefix` as `0`, representing the product from left to right.
   - `suffix` as `0`, representing the product from right to left.
5. We iterate through the array once. At each step:
   - `prefix = nums[i] * (prefix or 1)`
   - `suffix = nums[n-1-i] * (suffix or 1)`
   The expression `(prefix or 1)` resets the product to `1` whenever the previous product becomes `0`.
6. The prefix scan computes the product of subarrays from left to right, while the suffix scan computes the product from right to left.
7. Scanning in both directions is important because a maximum product subarray may start after a negative number or end before a negative number. One of the two scans will capture the optimal product.
8. After updating the prefix and suffix products, we compare both with the current answer and update:
   `res = max(res, prefix, suffix)`
9. Once the traversal is complete, `res` contains the largest product of any contiguous subarray. The time complexity is `O(n)` because the array is scanned once, and the auxiliary space complexity is `O(1)` since only a few variables are used."""