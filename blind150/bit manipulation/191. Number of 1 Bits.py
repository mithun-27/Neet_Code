#191. Number of 1 Bits
"""Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

 

Example 1:

Input: n = 11

Output: 3

Explanation:

The input binary string 1011 has a total of three set bits.

Example 2:

Input: n = 128

Output: 1

Explanation:

The input binary string 10000000 has a total of one set bit.

Example 3:

Input: n = 2147483645

Output: 30

Explanation:

The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

 

Constraints:

1 <= n <= 231 - 1
 

Follow up: If this function is called many times, how would you optimize it?"""

#answer:
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res



#example:
solution = Solution()
print(solution.hammingWeight(11))  # Output: 3
print(solution.hammingWeight(128))  # Output: 1
print(solution.hammingWeight(2147483645))  # Output: 30


"""Walkthrough:

1. We are given an integer `n` and need to count the number of `1` bits in its binary representation. This is called the Hamming Weight or population count.
2. We initialize `res = 0` to count how many set bits (`1`s) are present in the binary representation.
3. We use a `while n` loop, which continues as long as `n` is not zero.
4. Inside the loop, we execute `n &= n - 1`, which performs a bitwise AND between `n` and `n - 1`.
5. The key property of this operation is that it removes the rightmost set bit (`1`) from the binary representation of `n`.
6. For example, if `n = 12`, its binary representation is `1100`. Subtracting one gives `1011`, and performing `1100 & 1011` produces `1000`, removing the rightmost `1`.
7. After removing one set bit, we increment `res` by one because we have counted another `1` bit.
8. The loop repeats, removing one set bit during each iteration until all bits become zero.
9. Once `n` becomes zero, the loop terminates because there are no more set bits to count.
10. We return `res`, which contains the total number of `1` bits in the original number.
11. The key idea is that `n & (n - 1)` removes exactly one set bit per iteration, so we do not need to check every bit individually.
12. The time complexity is \\(O(k)\\), where \\(k\\) is the number of set bits in `n`, because the loop runs once for each `1` bit. The auxiliary space complexity is \\(O(1)\\) because only a single counter is used."""