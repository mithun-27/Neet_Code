#217. Contains Duplicate
"""Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109"""

#answer
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

#example 1:
nums = [1,2,3,1]
s = Solution()
print(s.containsDuplicate(nums)) # Output: true

#example 2:
nums = [1,2,3,4]
s = Solution()
print(s.containsDuplicate(nums)) # Output: false

"""walkthrough:
1. We initialize an empty set called seen to keep track of the unique numbers we have encountered in the array.
2. We iterate through each number in the input array nums.
3. For each number, we check if it is already in the seen set. If it is, that means we have encountered a duplicate, and we return True.
4. If the number is not in the seen set, we add it to the set.
5. If we finish iterating through the array without finding any duplicates, we return False, indicating that all elements are distinct.
This approach has a time complexity of O(n) and a space complexity of O(n) in the worst case, where n is the number of elements in the input array. The set allows for O(1) average time complexity for lookups and insertions, making it an efficient solution for this problem.   
"""