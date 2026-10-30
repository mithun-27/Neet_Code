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
n is even.
 

Follow up: If this function is called many times, how would you optimize it?"""


#answer:
class Solution:
    def reverseBits(self, n: int) -> int:
        res = n
        res = (res >> 16) | (res << 16) & 0xFFFFFFFF
        res = ((res & 0xff00ff00) >> 8) | ((res & 0x00ff00ff) << 8)
        res = ((res & 0xf0f0f0f0) >> 4) | ((res & 0x0f0f0f0f) << 4)
        res = ((res & 0xcccccccc) >> 2) | ((res & 0x33333333) << 2)
        res = ((res & 0xaaaaaaaa) >> 1) | ((res & 0x55555555) << 1)
        return res & 0xFFFFFFFF


#example:
solution = Solution()
print(solution.reverseBits(43261596))  # Output: 964176192
print(solution.reverseBits(2147483644))  # Output: 1073741822
print(solution.reverseBits(0))  # Output: 0


"""## Walkthrough:

1\. We are given a 32-bit unsigned integer `n`, and we need to reverse all its 32 bits. The first bit becomes the last bit, the second bit becomes the second-last bit, and so on.

2\. We initialize `res = n`. This creates a working variable `res` that stores the intermediate results while reversing the bits.

3\. We perform the first operation: `res = (res >> 16) | (res << 16) & 0xFFFFFFFF`.

4\. Here, `res >> 16` shifts the upper 16 bits to the lower 16-bit positions, while `res << 16` shifts the lower 16 bits to the upper 16-bit positions.

5\. The bitwise OR `|` combines these two parts, effectively swapping the upper 16 bits with the lower 16 bits.

6\. The mask `0xFFFFFFFF` represents 32 bits containing all `1`s. It ensures that the shifted result is restricted to 32 bits. In Python, the bitwise AND applies only to the left-shifted part because of operator precedence, but the final return also applies the mask.

7\. Next, we execute `res = ((res & 0xff00ff00) >> 8) | ((res & 0x00ff00ff) << 8)`.

8\. The mask `0xff00ff00` selects alternating groups of 8 bits, while `0x00ff00ff` selects the remaining groups of 8 bits.

9\. We shift the selected groups in opposite directions by 8 positions and combine them using bitwise OR. This swaps adjacent bytes.

10\. Next, we execute `res = ((res & 0xf0f0f0f0) >> 4) | ((res & 0x0f0f0f0f) << 4)`.

11\. The mask `0xf0f0f0f0` selects the upper 4 bits of every byte, while `0x0f0f0f0f` selects the lower 4 bits.

12\. We shift these groups in opposite directions by 4 positions and combine them. This swaps the upper and lower 4-bit groups inside every byte.

13\. Next, we execute `res = ((res & 0xcccccccc) >> 2) | ((res & 0x33333333) << 2)`.

14\. The mask `0xcccccccc` selects alternating 2-bit groups, while `0x33333333` selects the groups between them.

15\. We shift these groups in opposite directions by 2 positions and combine them. This swaps adjacent 2-bit groups throughout the 32-bit number.

16\. Finally, we execute `res = ((res & 0xaaaaaaaa) >> 1) | ((res & 0x55555555) << 1)`.

17\. The mask `0xaaaaaaaa` selects all bits in the even-numbered positions (counting from the right starting at position 0), while `0x55555555` selects all bits in the odd-numbered positions.

18\. We shift these selected bits in opposite directions by 1 position and combine them. This swaps every adjacent pair of bits, completing the reversal of all 32 bits.

19\. After all five stages, the bits are in completely reversed order: the original most significant bit becomes the least significant bit, and the original least significant bit becomes the most significant bit.

20\. We return `res & 0xFFFFFFFF` to ensure the final result contains only the lower 32 bits, keeping it within the required unsigned 32-bit range.

21\. The time complexity is \\(O(1)\\) because the algorithm performs a fixed number of bitwise operations, regardless of the input value.

22\. The auxiliary space complexity is \\(O(1)\\) because we use only a constant amount of extra space.

Key idea: Instead of reversing the bits one by one, we reverse them efficiently through five stages of bit swapping: 16-bit, 8-bit, 4-bit, 2-bit, and 1-bit swaps."""