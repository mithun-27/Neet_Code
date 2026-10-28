#338. Counting Bits
"""Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Do not solve it with built-in functions (i.e., like __builtin_popcount in C++).
 

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

0 <= n <= 105
 

Follow up:

It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?"""


#answer:
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp


#example:
solution = Solution()
print(solution.countBits(2))  # Output: [0, 1, 1]
print(solution.countBits(5))  # Output: [0, 1, 1, 2, 1, 2]
print(solution.countBits(10))  # Output: [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]


"""## Walkthrough:

1\. We are given an integer `n`, and we need to return an array `dp` where `dp[i]` represents the number of `1` bits in the binary representation of every number from `0` to `n`.

2\. We initialize the array using `dp = [0] * (n + 1)`. This creates an array of size `n + 1`, with every element initialized to `0`.

3\. We use `n + 1` because we need to calculate the number of set bits for all numbers from `0` through `n`, inclusive.

4\. We start a loop using `for i in range(n + 1)`. This iterates through every integer from `0` to `n`.

5\. For each number `i`, we calculate its number of set bits using `dp[i] = dp[i >> 1] + (i & 1)`.

6\. The expression `i >> 1` shifts the binary representation of `i` one position to the right. This is equivalent to integer division by `2`.

7\. The value `dp[i >> 1]` gives us the number of set bits in the number obtained after dividing `i` by `2`.

8\. The expression `i & 1` performs a bitwise AND operation with `1`. It returns `1` if `i` is odd and `0` if `i` is even.

9\. We add these two values because the number of set bits in `i` equals the number of set bits in `i >> 1`, plus the last bit of `i`.

10\. For example, when `i = 5`, its binary representation is `101`.

11\. We calculate `5 >> 1`, which gives `2`. The binary representation of `2` is `10`, which contains one set bit. Therefore, `dp[2] = 1`.

12\. Next, we calculate `5 & 1`, which gives `1` because `5` is odd.

13\. We then calculate `dp[5] = dp[2] + (5 & 1) = 1 + 1 = 2`. Therefore, the binary representation of `5` contains two set bits.

14\. When `i = 4`, its binary representation is `100`. We calculate `4 >> 1 = 2` and `4 & 1 = 0`. Therefore, `dp[4] = dp[2] + 0 = 1`.

15\. When `i = 0`, both `0 >> 1` and `0 & 1` equal `0`. Therefore, `dp[0] = dp[0] + 0 = 0`, which is correct because zero contains no set bits.

16\. Since the loop processes numbers in increasing order, `dp[i >> 1]` has already been calculated before it is used. This allows us to solve the problem using dynamic programming.

17\. After the loop finishes, the array contains the number of set bits for every integer from `0` to `n`.

18\. Finally, `return dp` returns the completed array.

19\. For example, if `n = 5`, the output is `[0, 1, 1, 2, 1, 2]`.

20\. The time complexity is \\(O(n)\\) because we process each number from `0` to `n` exactly once.

21\. The auxiliary space complexity is \\(O(n)\\) because the `dp` array stores `n + 1` values."""