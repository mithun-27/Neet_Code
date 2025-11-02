#217. Contains Duplicate - Explanation

"""Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false"""

#answer

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap=set()
        for num in nums:
            if num in hashmap:
                return True
            hashmap.add(num)
        return False
    
#example usage
solution = Solution()
print(solution.containsDuplicate([1, 2, 3, 3]))  # Output: True
print(solution.containsDuplicate([1, 2, 3, 4]))  # Output: False

"""walkthrough
1. We define a class Solution with a method containsDuplicate that takes a list of integers nums as input.
2. We initialize an empty set called hashmap to keep track of the unique numbers we encounter as we iterate through the list.
3. We loop through each number num in the input list nums.
4. Inside the loop, we check if the current number num is already in the hashmap set.
   - If it is, we return True immediately, indicating that we have found a duplicate.
   - If it is not, we add the number num to the hashmap set.
5. If we finish iterating through the entire list without finding any duplicates, we return False, indicating that all numbers in the list are unique."""