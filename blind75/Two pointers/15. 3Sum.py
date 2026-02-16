#15. 3Sum
"""Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = [0,1,1]
Output: []
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105"""

#answer
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res
    
#example usage
solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4]))  # Output: [[-1,-1,2],[-1,0,1]]
print(solution.threeSum([0,1,1]))  # Output: []
print(solution.threeSum([0,0,0]))  # Output: [[0,0,0]]  

"""WALKTHROUGH
1. We define a class Solution with a method threeSum that takes a list of integers nums as input.
2. We initialize an empty list res to store the resulting triplets and sort the input list nums.
3. We use a for loop to iterate through the sorted list nums, where i is the index and a is the value at that index.
4. If a is greater than 0, we break the loop since we cannot find any triplet that sums to zero.
5. We check if the current value a is the same as the previous value to avoid duplicate triplets. If it is, we continue to the next iteration.  
6. We initialize two pointers, l and r, to the indices immediately after i and at the end of the list, respectively.
7. We use a while loop to check the sum of the three numbers (a, nums[l], nums[r]). If the sum is greater than 0, we move the right pointer r to the left. If the sum is less than 0, we move the left pointer l to the right. If the sum is exactly 0, we have found a valid triplet, and we add it to the result list res.    
8. After finding a valid triplet, we move both pointers l and r to continue searching for other potential triplets. We also skip over any duplicate values at the left pointer to avoid adding duplicate triplets to the result.    
9. Finally, we return the list of triplets res that sum to zero.
"""