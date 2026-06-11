#704. Binary Search
"""Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order."""

#answer
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            m = l + ((r - l) // 2)
            if nums[m] >= target:
                r = m
            elif nums[m] < target:
                l = m + 1
        return l if (l < len(nums) and nums[l] == target) else -1
    
#example 1:
"""Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4  """  
#example 2:
"""Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1  """

"""walkthrough:
1. We initialize two pointers, l and r, to represent the left and right boundaries of our search space. Initially, l is set to 0 (the index of the first element) and r is set to the length of the nums array (one past the last index).   
2. We enter a while loop that continues as long as l is less than r. This loop will help us narrow down our search space until we find the target or determine that it does not exist in the array. 
3. Inside the loop, we calculate the middle index m using the formula l + ((r - l) // 2). This formula helps prevent potential overflow issues that can arise with large indices.       
4. We then compare the value at index m (nums[m]) with the target. If nums[m] is greater than or equal to the target, it means that the target must be in the left half of the current search space (including m), so we update r to m. If nums[m] is less than the target, it means that the target must be in the right half of the current search space (excluding m), so we update l to m + 1.
5. After the loop terminates, we check if l is within the bounds of the array and if the value at index l is equal to the target. If both conditions are true, we return l as the index of the target. Otherwise, we return -1 to indicate that the target does not exist in the array.                     
This algorithm efficiently searches for the target in a sorted array with a time complexity of O(log n) and a space complexity of O(1).
"""