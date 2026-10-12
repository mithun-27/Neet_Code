#43. Multiply Strings
"""Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
 

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself."""


#answer:
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"

        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                res[i1 + i2] += digit
                res[i1 + i2 + 1] += res[i1 + i2] // 10
                res[i1 + i2] = res[i1 + i2] % 10

        res, beg = res[::-1], 0
        while beg < len(res) and res[beg] == 0:
            beg += 1
        res = map(str, res[beg:])
        return "".join(res)

#example:
s = Solution()
print(s.multiply("2", "3"))  # Output: "6"
print(s.multiply("123", "456"))  # Output: "56088"
print(s.multiply("0", "123"))  # Output: "0"


"""Walkthrough:

1. We are given two non-negative integers as strings, `num1` and `num2`, and need to multiply them without converting the entire strings into integers or using a built-in multiplication method.
2. We first check whether either number is `"0"`. If so, the product is `"0"`, so we return immediately.
3. We create a result array `res` of size `len(num1) + len(num2)`, initialized with zeros, because multiplying numbers with `m` and `n` digits produces at most `m + n` digits.
4. We reverse both input strings using `num1[::-1]` and `num2[::-1]` so that the units digits come first, making it easier to calculate each digit's contribution to the product.
5. We use two nested loops to multiply every digit of `num1` by every digit of `num2`. The outer loop selects a digit from `num1`, while the inner loop selects a digit from `num2`.
6. For each pair of digits, we calculate their product using `digit = int(num1[i1]) * int(num2[i2])`.
7. We add this product to `res[i1 + i2]`, because multiplying digits at positions `i1` and `i2` contributes to position `i1 + i2` in the result.
8. We handle the carry by adding `res[i1 + i2] // 10` to the next position, `res[i1 + i2 + 1]`.
9. We then keep only the current digit by applying `res[i1 + i2] %= 10`, ensuring that each position contains a single decimal digit after carry handling.
10. After all digit pairs have been multiplied, we reverse the result array using `res[::-1]` to restore the normal left-to-right order of the product.
11. We initialize `beg = 0` and skip leading zeros by incrementing `beg` while the current digit is zero.
12. We convert the remaining digits into strings using `map(str, res[beg:])` and combine them with `"".join(...)` to produce the final product as a string.
13. The key idea is to simulate elementary school multiplication: multiply individual digits, accumulate their contributions in the correct positions, propagate carries, and remove leading zeros.
14. The time complexity is \\(O(m \times n)\\) because every digit in `num1` is multiplied by every digit in `num2`, where `m` and `n` are their lengths.
15. The auxiliary space complexity is \\(O(m+n)\\) because the result array stores up to `m+n` digits."""