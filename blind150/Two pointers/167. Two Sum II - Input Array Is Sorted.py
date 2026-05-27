#167. Two Sum II - Input Array Is Sorted
"""Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 

Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution."""

#answer
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []
    
#example 1:
solution = Solution()   
print(solution.twoSum([2,7,11,15], 9)) # Output: [1,2]
#example 2:
print(solution.twoSum([2,3,4], 6)) # Output: [1,3]
#example 3:
print(solution.twoSum([-1,0], -1)) # Output: [1,2]

"""walkthrough:
1. We initialize two pointers, l and r, to the start and end of the numbers array, respectively.    
2. We enter a loop that continues until the two pointers meet.
3. Inside the loop, we calculate the current sum of the numbers at the two pointers. If the current sum is greater than the target, we move the right pointer left to decrease the sum. If the current sum is less than the target, we move the left pointer right to increase the sum. If the current sum equals the target, we return the indices of the two numbers (adjusted for 1-indexing).   
4. If we exit the loop without finding a solution, we return an empty array (though the problem guarantees that there will be exactly one solution).    
This algorithm runs in O(n) time, where n is the length of the numbers array, because in the worst case we may need to check each element once. The space complexity is O(1) since we are using only a constant amount of extra space for the pointers and the output array. """        
