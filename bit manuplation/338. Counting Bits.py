#338. Counting Bits
"""Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 

Constraints:

0 <= n <= 105"""

#answer
from git import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp
    
#example 1:
n = 2
s = Solution()
print(s.countBits(n)) # Output: [0,1,1]

#example 2:
n = 5
print(s.countBits(n)) # Output: [0,1,1,2,1,2]


"""walkthrough:
1. We initialize a list `dp` of length `n + 1` with all elements set to 0. This list will store the number of set bits for each integer from 0 to n.    
2. We iterate through each integer `i` from 0 to n. For each integer, we calculate the number of set bits using the formula `dp[i] = dp[i >> 1] + (i & 1)`.
   - `i >> 1` is equivalent to dividing `i` by 2, which effectively shifts the bits of `i` to the right by one position. This gives us the number of set bits in the integer `i` without its least significant bit.
   - `i & 1` checks if the least significant bit of `i` is set (i.e., if it is 1). If it is, we add 1 to the count of set bits.
3. After the loop, we return the list `dp`, which contains the number of set bits for each integer from 0 to n.
The time complexity of this solution is O(n) since we iterate through all integers from 0 to n once, and the space complexity is also O(n) due to the `dp` list storing the results for each integer.   
"""