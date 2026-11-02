#7. Reverse Integer
"""Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1"""


#answer:
class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648  # -2^31,
        MAX = 2147483647  #  2^31 - 1

        res = 0
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0
            if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
                return 0
            res = (res * 10) + digit

        return res



#example:
solution = Solution()   
print(solution.reverse(123))  # Output: 321
print(solution.reverse(-123))  # Output: -321
print(solution.reverse(120))  # Output: 21


"""## Walkthrough:

1\. We are given a signed 32-bit integer `x`, and we need to reverse its digits while preserving its sign.

2\. If the reversed number goes outside the signed 32-bit integer range, we must return `0`.

3\. We initialize `MIN = -2147483648`, which represents the minimum signed 32-bit integer (\\(-2^{31}\\)).

4\. We initialize `MAX = 2147483647`, which represents the maximum signed 32-bit integer (\\(2^{31}-1\\)).

5\. We initialize `res = 0`. This variable stores the reversed number as we build it digit by digit.

6\. We start a `while` loop using `while x`. The loop continues as long as `x` is not equal to zero.

7\. Inside the loop, we calculate `digit = int(math.fmod(x, 10))`.

8\. The `math.fmod(x, 10)` operation extracts the last digit of `x`. Unlike the modulo operator in Python, `fmod` preserves the sign of the dividend.

9\. For example, if `x = 123`, the extracted digit is `3`. If `x = -123`, the extracted digit is `-3`.

10\. Next, we execute `x = int(x / 10)`. This removes the last digit from `x` by dividing it by `10` and converting the result to an integer. Python's `int()` truncates the result towards zero.

11\. Next, we check whether adding the extracted digit to `res` would cause a positive integer overflow using `if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10)`.

12\. Here, `MAX // 10` gives `214748364`, and `MAX % 10` gives `7`. If `res` is already greater than `214748364`, multiplying it by `10` would exceed the maximum allowed value.

13\. If `res` equals `214748364`, we check whether the next digit is greater than `7`. If it is, the reversed number would exceed the maximum 32-bit integer.

14\. If either positive overflow condition is true, we immediately return `0`.

15\. Next, we check for negative integer overflow using `if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10)`.

16\. Here, `MIN // 10` gives `-214748365`, and `MIN % 10` gives `2` in Python. If `res` is smaller than `-214748365`, multiplying it by `10` would go below the minimum allowed value.

17\. If `res` equals `-214748365`, we check whether the next digit is less than `2`. If it is, the reversed number would exceed the negative 32-bit limit.

18\. If either negative overflow condition is true, we immediately return `0`.

19\. If neither overflow condition is satisfied, we update `res = (res * 10) + digit`. This shifts the existing digits one position to the left and appends the newly extracted digit.

20\. For example, if `x = 123`, initially `res = 0`. We extract `3`, so `res = 3`. Next, we extract `2`, so `res = 32`. Finally, we extract `1`, so `res = 321`.

21\. The loop continues until all digits have been extracted and `x` becomes `0`.

22\. Finally, `return res` returns the reversed integer.

23\. The time complexity is \\(O(\log\_{10}|x|)\\) because we process each digit exactly once. The number of digits in `x` determines the number of iterations.

24\. The auxiliary space complexity is \\(O(1)\\) because we use only a fixed number of variables without creating additional data structures.

Key idea: Extract the last digit using `math.fmod()`, remove it from the original number, and append it to the reversed result. Before every update, check the positive and negative 32-bit limits to prevent integer overflow."""