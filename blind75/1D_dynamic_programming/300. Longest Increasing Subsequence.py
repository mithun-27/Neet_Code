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

#answer
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
    
#example 1:
nums = [10,9,2,5,3,7,101,18]
print(Solution().lengthOfLIS(nums)) #4

#example 2:
nums = [0,1,0,3,2,3]
print(Solution().lengthOfLIS(nums)) #4

#example 3:
nums = [7,7,7,7,7,7,7]
print(Solution().lengthOfLIS(nums)) #1

"""walkthrough the code:
1. We initialize an empty list `dp` to store the longest increasing subsequence found so far. We start by adding the first element of `nums` to `dp`.
2. We also initialize a variable `LIS` to keep track of the length of the longest increasing subsequence, starting at 1 since we have at least one element in `dp`.
3. We iterate through the `nums` array starting from the second element. For each element, we check if it is greater than the last element in `dp`. If it is, we append it to `dp` and increment the `LIS` counter.
4. If the current element is not greater than the last element in `dp`, we use the `bisect_left` function to find the index in `dp` where the current element should be placed to maintain the increasing order. We then replace the element at that index in `dp` with the current element.
5. Finally, we return the value of `LIS`, which represents the length of the longest increasing subsequence found in the input array `nums`.
The `bisect_left` function is used to maintain the order of the `dp` list and ensures that we are always replacing the correct element in `dp` to keep it sorted. This approach allows us to efficiently find the length of the longest increasing subsequence in O(n log n) time complexity."""