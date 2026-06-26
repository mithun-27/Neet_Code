#287. Find the Duplicate Number
"""Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [3,3,3,3,3]
Output: 3
 

Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
 

Follow up:

How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?"""

#answer
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
            
#example:1
"""Input: nums = [1,3,4,2,2]
Output: 2"""
#example:2
"""Input: nums = [3,1,3,4,2]
Output: 3"""
#example:3
"""Input: nums = [3,3,3,3,3]        
Output: 3"""    

"""walkthrough:
1. Initialize two pointers, slow and fast, both starting at the first index of the array.
2. Move the slow pointer one step at a time (slow = nums[slow]) and the fast pointer two steps at a time (fast = nums[nums[fast]]) until they meet. This meeting point indicates that there is a cycle in the array, which is caused by the duplicate number.
3. Once a cycle is detected, initialize a new pointer, slow2, starting at the first index of the array.
4. Move both slow and slow2 one step at a time until they meet. The meeting point will be the duplicate number in the array.
5. Return the value at the meeting point, which is the duplicate number.    
6. The time complexity of this solution is O(n), where n is the length of the array. The space complexity is O(1) since we are using only a constant amount of extra space for the pointers."""