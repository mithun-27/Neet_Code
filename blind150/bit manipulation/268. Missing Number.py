# Bit Manipulation Solution
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
All the numbers of nums are unique.
 

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?"""


#answer:
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += i - nums[i]
        return res


#example:   
solution = Solution()
print(solution.missingNumber([3, 0, 1]))  # Output: 2
print(solution.missingNumber([0, 1]))     # Output: 2
print(solution.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # Output: 8



"""## Walkthrough:

1\. We are given an array `nums` containing `n` distinct numbers from the range `0` to `n`. One number is missing, and we need to find and return that missing number.

2\. We initialize `res = len(nums)`. This stores the length of the array, which is `n`.

3\. We initialize `res` with `n` because the numbers in the expected range go from `0` to `n`, inclusive.

4\. We start a `for` loop using `for i in range(len(nums))`. This iterates through every index of the array, starting from `0` to `n - 1`.

5\. Inside the loop, we execute `res += i - nums[i]`.

6\. Here, `i` represents the expected number at that position, while `nums[i]` represents the actual number present in the array.

7\. We subtract the actual number from the expected number and add the difference to `res`.

8\. By doing this for every index, we calculate the difference between the sum of expected numbers and the sum of actual array elements.

9\. Let's take an example: `nums = [3, 0, 1]`.

10\. The length of the array is `3`, so initially, `res = 3`.

11\. In the first iteration, `i = 0` and `nums[0] = 3`. We calculate `res = 3 + (0 - 3) = 0`.

12\. In the second iteration, `i = 1` and `nums[1] = 0`. We calculate `res = 0 + (1 - 0) = 1`.

13\. In the third iteration, `i = 2` and `nums[2] = 1`. We calculate `res = 1 + (2 - 1) = 2`.

14\. After completing the loop, `res = 2`. Therefore, the missing number is `2`.

15\. The algorithm works because the sum of all numbers from `0` to `n` should be equal to the sum of the array elements plus the missing number.

16\. Finally, `return res` returns the missing number.

17\. The time complexity is \\(O(n)\\) because we iterate through the array exactly once.

18\. The auxiliary space complexity is \\(O(1)\\) because we use only one extra variable, `res`, without creating another array or data structure.

Key idea: We start with `n` and add the difference between each index and its corresponding array value. This calculates the missing number without sorting the array or using extra space."""