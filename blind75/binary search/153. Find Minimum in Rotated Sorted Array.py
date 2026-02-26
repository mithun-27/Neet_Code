#153. Find Minimum in Rotated Sorted Array
"""Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 

Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times."""

#answer
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]

#example usage
sol = Solution()
print(sol.findMin([3,4,5,1,2])) #1
print(sol.findMin([4,5,6,7,0,1,2])) #0
print(sol.findMin([11,13,15,17])) #11

"""walkthrough:
1. We initialize two pointers, `l` and `r`, to the start and end of the array, respectively.
2. We enter a while loop that continues until `l` is less than `r`.
3. Inside the loop, we calculate the middle index `m` as the average of `l` and `r`.
4. We compare the middle element `nums[m]` with the rightmost element `nums[r]`.
   - If `nums[m]` is less than `nums[r]`, it means the minimum element is in the left half of the array (including `m`), so we move the right pointer `r` to `m`.
   - Otherwise, it means the minimum element is in the right half of the array (excluding `m`), so we move the left pointer `l` to `m + 1`.
5. After the loop, `l` will be pointing to the minimum element in the array, so we return `nums[l]`.
6. The time complexity of this solution is O(log n) due to the binary search approach, and the space complexity is O(1) since we are using only a constant amount of extra space.   
"""