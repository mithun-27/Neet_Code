#268. Missing Number
"""Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

Example 1:

Input: nums = [3,0,1]

Output: 2

Explanation:

n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:

Input: nums = [0,1]

Output: 2

Explanation:

n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]

Output: 8

Explanation:

n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

 
 

 

 

Constraints:

n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique."""

#answer
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += i - nums[i]
        return res
    
#example 1:
nums = [3,0,1]
s = Solution()
print(s.missingNumber(nums)) # Output: 2

#example 2:
nums = [0,1]
print(s.missingNumber(nums)) # Output: 2

#example 3:
nums = [9,6,4,2,3,5,7,0,1]
print(s.missingNumber(nums)) # Output: 8

"""walkthrough:
1. We initialize a variable `res` with the value of the length of the input array `nums`. This is because the missing number can be at most `n`, which is equal to the length of the array. 
2. We then iterate through the array using a for loop. For each index `i`, we add `i` to `res` and subtract the value at `nums[i]` from `res`. This effectively adds all the indices from 0 to n-1 and subtracts all the numbers present in the array.
3. After the loop, `res` will contain the value of the missing number, which we return.
The time complexity of this solution is O(n) since we iterate through the array once. The space complexity is O(1) since we use only a constant amount of extra space for the variable `res`.
"""