#136. Single Number
"""Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]

Output: 1

Example 2:

Input: nums = [4,1,2,1,2]

Output: 4

Example 3:

Input: nums = [1]

Output: 1

 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once."""

#answer:
from ast import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res = num ^ res
        return res


#example:
solution = Solution()
print(solution.singleNumber([2, 2, 1]))  # Output: 1
print(solution.singleNumber([4, 1, 2, 1, 2]))  # Output: 4
print(solution.singleNumber([1]))  # Output: 1


"""Walkthrough:

1. We are given an integer array `nums` in which every element appears exactly twice except for one element that appears only once. Our goal is to find that unique element.
2. We initialize `res = 0` to store the result. The value `0` is used because XOR with zero leaves a number unchanged.
3. We iterate through every number in the array using `for num in nums`.
4. For each number, we perform the XOR operation using `res = num ^ res`, which compares the binary bits of `num` and `res`.
5. The XOR operator follows three important properties: `a ^ a = 0`, `a ^ 0 = a`, and XOR is commutative and associative, meaning the order of operations does not affect the final result.
6. When the same number appears twice, XOR cancels both occurrences because `num ^ num = 0`.
7. As the loop processes the array, all duplicate numbers cancel each other out, leaving only the number that appears once.
8. For example, if `nums = [4, 1, 2, 1, 2]`, the XOR operations become `0 ^ 4 ^ 1 ^ 2 ^ 1 ^ 2`.
9. The duplicate `1`s cancel each other, and the duplicate `2`s also cancel each other, leaving `4`.
10. After processing every element, we return `res`, which contains the unique number.
11. The key idea is to use XOR to eliminate duplicate values without sorting the array or using an additional data structure.
12. The time complexity is \\(O(n)\\) because every element is processed exactly once, and the auxiliary space complexity is \\(O(1)\\) because only one variable is used."""