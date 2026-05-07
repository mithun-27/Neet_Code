#190. Reverse Bits
"""Reverse bits of a given 32 bits signed integer.

 

Example 1:

Input: n = 43261596

Output: 964176192

Explanation:

Integer	Binary
43261596	00000010100101000001111010011100
964176192	00111001011110000010100101000000
Example 2:

Input: n = 2147483644

Output: 1073741822

Explanation:

Integer	Binary
2147483644	01111111111111111111111111111100
1073741822	00111111111111111111111111111110
 

Constraints:

0 <= n <= 231 - 2
n is even."""
#answer
class Solution:
    def reverseBits(self, n: int) -> int:
        res = n
        res = (res >> 16) | (res << 16) & 0xFFFFFFFF
        res = ((res & 0xff00ff00) >> 8) | ((res & 0x00ff00ff) << 8)
        res = ((res & 0xf0f0f0f0) >> 4) | ((res & 0x0f0f0f0f) << 4)
        res = ((res & 0xcccccccc) >> 2) | ((res & 0x33333333) << 2)
        res = ((res & 0xaaaaaaaa) >> 1) | ((res & 0x55555555) << 1)
        return res & 0xFFFFFFFF
    
#example 1:
n = 43261596
s = Solution()
print(s.reverseBits(n)) # Output: 964176192

#example 2:
n = 2147483644
print(s.reverseBits(n)) # Output: 1073741822

"""walkthrough:
1. We initialize a variable `res` with the value of `n`. This variable will be used to store the intermediate results as we reverse the bits.   
2. We perform a series of bitwise operations to reverse the bits in `res`. The operations are as follows:
   - We first swap the left and right 16 bits of `res` using a combination of right and left shifts, and a bitwise OR operation.
   - Next, we swap the 8-bit groups within the 16-bit halves using a similar approach.
   - We continue this process by swapping 4-bit groups, then 2-bit groups, and finally individual bits.
3. After all the swaps, we return the final value of `res`, ensuring that it is treated as a 32-bit unsigned integer by applying a bitwise AND with `0xFFFFFFFF`.
The time complexity of this solution is O(1) since we perform a fixed number of operations regardless of the input size. The space complexity is also O(1) since we use only a constant amount of extra space for the variable `res`.
"""