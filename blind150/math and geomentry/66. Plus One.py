#66. Plus One
"""You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
 

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's."""

#answer:
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + digits


#example:
s = Solution()
print(s.plusOne([1, 2, 3]))  # Output: [1, 2, 4]
print(s.plusOne([4, 3, 2, 1]))  # Output: [4, 3, 2, 2]
print(s.plusOne([9]))  # Output: [1, 0] 


"""Walkthrough:

1. We are given an array `digits` representing a non-negative integer, and we need to add `1` to that number and return the result as an array of digits.

2. We start by calculating `n = len(digits)` to determine the number of digits in the given number.

3. We iterate through the array from right to left, starting from the last digit, because addition begins at the units place.

4. At each position `i`, we check whether `digits[i]` is less than `9`.

5. If the current digit is less than `9`, we increment it by `1` and immediately return the updated array because no carry is required.

6. If the current digit is `9`, adding `1` makes it `10`, so we set that digit to `0` and carry the extra `1` to the previous digit.

7. We continue moving left, setting consecutive `9`s to `0` until we find a digit smaller than `9` or reach the beginning of the array.

8. If we find a digit smaller than `9`, we increment it and return the array with all necessary carry operations completed.

9. If every digit is `9`, all digits become `0`, and the loop finishes without returning.

10. In this case, we create a new array using `[1] + digits`, which places `1` at the beginning to represent the additional digit created by the carry.

11. For example, if `digits = [1, 2, 9]`, the last digit becomes `0`, the previous digit becomes `3`, and the result is `[1, 3, 0]`.

12. If `digits = [9, 9, 9]`, every digit becomes `0`, and adding `1` at the beginning produces `[1, 0, 0, 0]`.

13. The key idea is to process digits from right to left, propagate the carry only when the current digit is `9`, and stop as soon as the carry is resolved.

14. The time complexity is O(n) in the worst case because every digit may need to be processed.

15. The auxiliary space complexity is O(1) when the existing array is updated in-place; however, the all-`9` case creates a new array requiring O(n) additional space.
"""