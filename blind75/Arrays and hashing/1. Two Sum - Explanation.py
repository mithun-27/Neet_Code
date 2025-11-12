# Two Sum 

"""Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:

Input: nums = [4,5,6], target = 10

Output: [0,2]
Example 3:

Input: nums = [5,5], target = 10

Output: [0,1]
Constraints:

2 <= nums.length <= 1000
-10,000,000 <= nums[i] <= 10,000,000
-10,000,000 <= target <= 10,000,000"""


#answer

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i
        return []
    
#example usage
solution = Solution()
print(solution.twoSum([3, 4, 5, 6], 7))  # Output: [0, 1]
print(solution.twoSum([4, 5, 6], 10))     # Output: [0, 2]
print(solution.twoSum([5, 5], 10))        # Output: [0, 1]

"""walkthrough
1. We define a class Solution with a method twoSum that takes a list of integers nums and an integer target as input.
2. We initialize an empty dictionary called hashmap to store the numbers we have seen so far along with their indices.
3. We loop through the list nums using enumerate to get both the index i and the number num.
4. For each number num, we calculate its complement by subtracting num from the target.
5. We check if the complement is already in the hashmap:
   - If it is, we return a list containing the index of the complement (from the hashmap) and the current index i.
   - If it is not, we add the current number num and its index i to the hashmap.
6. If we finish iterating through the entire list without finding a valid pair, we return an empty list (though the problem guarantees that there will always be a solution).
"""