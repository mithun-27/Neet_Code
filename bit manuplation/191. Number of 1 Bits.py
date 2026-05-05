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

#answer
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res
    
#example 1:
n = 11
s = Solution()
print(s.hammingWeight(n)) # Output: 3

#example 2:
n = 128
print(s.hammingWeight(n)) # Output: 1

"""walkthrough:
1. Initialize a variable `res` to 0, which will keep track of the number of set bits.
2. Use a while loop that continues until `n` becomes 0.
3. In each iteration, perform `n &= n - 1` to remove the rightmost set bit from `n`.
4. Increment `res` by 1 in each iteration.
5. Return `res` as the final result.
This approach is efficient because it directly counts the number of set bits by removing them one by one, resulting in a time complexity of O(k), where k is the number of set bits in `n`."""