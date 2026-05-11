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

"""walkthrough:
1. We define a mask to handle 32-bit integer overflow and a max_int to determine if the result is negative.
2. We use a while loop that continues until there are no more carries (b becomes 0).
3. Inside the loop, we calculate the carry by performing a bitwise AND between a and b, then left-shift the result by 1 to prepare for the next addition.
4. We update a to be the result of a bitwise XOR between a and b, which gives us the sum without the carry.
5. We update b to be the carry, which will be added in the next iteration.  
6. After the loop, we check if a is greater than max_int. If it is, it means the result is negative, and we return the two's complement of a. Otherwise, we return a as the final result.
This method effectively simulates the addition process using bitwise operations, allowing us to compute the sum without using the + operator."""