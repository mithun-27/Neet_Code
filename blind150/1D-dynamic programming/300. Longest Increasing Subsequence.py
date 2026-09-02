#300. Longest Increasing Subsequence
"""Given an integer array nums, return the length of the longest strictly increasing subsequence.

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104"""

#answer:
from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        dp.append(nums[0])

        LIS = 1
        for i in range(1, len(nums)):
            if dp[-1] < nums[i]:
                dp.append(nums[i])
                LIS += 1
                continue

            idx = bisect_left(dp, nums[i])
            dp[idx] = nums[i]

        return LIS


#example:
"""Input
nums =
[10,9,2,5,3,7,101,18]
Output
4
Expected
4"""


"""Walkthrough:
1. We want to find the length of the longest strictly increasing subsequence (LIS) in the given array `nums`.
2. Instead of storing every possible subsequence, we maintain a list `dp` where `dp[i]` represents the smallest possible ending value of an increasing subsequence of length `i + 1`.
3. We start by putting the first element `nums[0]` into `dp`. At this point, the longest increasing subsequence has length `1`.
4. We iterate through the remaining elements of `nums`. If the current number is greater than the last element of `dp`, we can extend the current longest increasing subsequence, so we append the number to `dp` and increase `LIS` by `1`.
5. If the current number is smaller than or equal to the last element of `dp`, we cannot directly extend the subsequence. Instead, we use `bisect_left()` to find the first position in `dp` whose value is greater than or equal to the current number.
6. We replace the value at that position with the current number. This does not necessarily change the actual LIS, but it gives future elements a smaller value to build an increasing subsequence from.
7. The important idea is that `dp` does not store the actual longest subsequence. It stores the smallest possible tail values for increasing subsequences of different lengths, which allows us to efficiently determine the maximum length.
8. We continue processing every element. The variable `LIS` keeps track of the length of the longest increasing subsequence found so far, so after processing the entire array, we return `LIS`.
9. The time complexity is `O(n log n)` because each element requires a binary search using `bisect_left()`, and the auxiliary space complexity is `O(n)` for the `dp` list."""