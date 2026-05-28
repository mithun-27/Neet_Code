#15. 3Sum
"""Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105"""


#answer
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
    
#example 1:
solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4])) # Output: [[-1,-1,2],[-1,0,1]]
#example 2:
print(solution.threeSum([0,1,1])) # Output: []
#example 3:
print(solution.threeSum([0,0,0])) # Output: [[0,0,0]]

"""walkthrough: 
1. We initialize an empty list res to store the resulting triplets.
2. We sort the input array nums to facilitate the two-pointer approach and to easily skip duplicates.
3. We iterate through the sorted array using a for loop, where i is the index and a is the value at that index.
4. If a is greater than 0, we can break the loop since any further triplets will also be greater than 0.
5. If i is greater than 0 and a is the same as the previous element, we skip the current iteration to avoid duplicate triplets.
6. We initialize two pointers, l and r, to the positions immediately after i and at the end of the array, respectively.
7. We enter a while loop that continues until the two pointers meet.    
8. Inside the loop, we calculate the sum of a, nums[l], and nums[r]. If the sum is greater than 0, we move the right pointer left to decrease the sum. If the sum is less than 0, we move the left pointer right to increase the sum. If the sum equals 0, we have found a valid triplet, which we add to res. We then move both pointers and skip any duplicate values to avoid repeating triplets.
9. Finally, we return the list of triplets res.
10. The time complexity of this solution is O(n^2) due to the nested loops, and the space complexity is O(1) if we ignore the space used for the output list."""    