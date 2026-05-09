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

#answer
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        return a if a <= max_int else ~(a ^ mask)
    
#example 1:
a = 1
b = 2
s = Solution()
print(s.getSum(a, b)) # Output: 3

#example 2:
a = 2
b = 3
s = Solution()
print(s.getSum(a, b)) # Output: 5