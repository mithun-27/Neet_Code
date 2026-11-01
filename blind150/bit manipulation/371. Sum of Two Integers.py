#371. Sum of Two Integers
"""Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = 2, b = 3
Output: 5
 

Constraints:

-1000 <= a, b <= 1000"""


#answer:
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        return a if a <= max_int else ~(a ^ mask)


#example:
solution = Solution()           
print(solution.getSum(1, 2))  # Output: 3
print(solution.getSum(2, 3))  # Output: 5   
print(solution.getSum(-1, 1))  # Output: 0


"""## Walkthrough:

1\. We are given two integers `a` and `b`, and we need to calculate their sum without using the `+` or `-` operators.

2\. We use bitwise operations to perform addition by calculating the sum bits and carry bits separately.

3\. We initialize `mask = 0xFFFFFFFF`. This hexadecimal value represents 32 bits containing all `1`s. It ensures that our calculations stay within the 32-bit range.

4\. We initialize `max_int = 0x7FFFFFFF`. This represents the maximum signed 32-bit integer, which is `2147483647`.

5\. We start a `while` loop using `while b != 0`. The loop continues until there are no more carry bits to process.

6\. Inside the loop, we calculate `carry = (a & b) << 1`.

7\. The bitwise AND operation `a & b` identifies the positions where both numbers contain `1`. These positions generate carry bits during binary addition.

8\. We shift the carry one position to the left using `<< 1` because a carry generated at one position must be added to the next higher position.

9\. Next, we calculate `a = (a ^ b) & mask`.

10\. The bitwise XOR operation `a ^ b` calculates the sum bits without considering the carry. XOR produces `1` when the two corresponding bits are different.

11\. We apply `& mask` to restrict the result to 32 bits, preventing Python's unlimited-size integers from affecting the intended 32-bit arithmetic.

12\. Next, we calculate `b = carry & mask`. This stores the carry bits for the next iteration and also restricts them to 32 bits.

13\. The loop repeats because the newly calculated carry may generate additional carry bits when added to the current result.

14\. When `b` becomes `0`, there are no remaining carry bits. Therefore, `a` contains the final 32-bit result.

15\. Finally, we execute `return a if a <= max_int else ~(a ^ mask)`.

16\. Here, we check whether `a` is within the positive signed 32-bit integer range. If `a <= max_int`, we directly return `a`.

17\. Otherwise, the result represents a negative number in 32-bit two's complement form. We convert it into Python's negative integer representation using `~(a ^ mask)`.

18\. For example, if `a = -5` and `b = 3`, the expected result is `-2`. The bitwise operations perform the addition through XOR and carry propagation, and the final conversion returns `-2`.

19\. The time complexity is \\(O(1)\\) because the algorithm operates on a fixed 32-bit representation. At most a constant number of carry-propagation iterations are required.

20\. The auxiliary space complexity is \\(O(1)\\) because we use only a fixed number of variables, regardless of the input values.

Key idea: XOR calculates the sum without carry, while AND followed by a left shift calculates the carry. Repeating these operations until the carry becomes zero gives the final sum without using arithmetic addition or subtraction."""