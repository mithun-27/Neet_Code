#202. Happy Number
"""Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false
 

Constraints:

1 <= n <= 231 - 1"""


#answer:
class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumOfSquares(n)
        power = lam = 1

        while slow != fast:
            if power == lam:
                slow = fast
                power *= 2
                lam = 0
            fast = self.sumOfSquares(fast)
            lam += 1
        return True if fast == 1 else False

    def sumOfSquares(self, n: int) -> int:
        output = 0

        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output


#example:
s = Solution()
print(s.isHappy(19))  # Output: True
print(s.isHappy(2))   # Output: False   
print(s.isHappy(7))   # Output: True


"""Walkthrough:

1. We are given a positive integer `n` and need to determine whether it is a Happy Number. A number is happy if repeatedly replacing it with the sum of the squares of its digits eventually leads to `1`.

2. The solution uses Floyd’s Cycle Detection Algorithm, also known as the Tortoise and Hare algorithm, to detect cycles in the sequence without storing previously seen numbers in a set.

3. The helper function `sumOfSquares(n)` calculates the sum of the squares of all digits of `n`.

4. Inside `sumOfSquares()`, `n % 10` extracts the last digit, `digit ** 2` squares it, and `output += digit` adds the squared value to the total.

5. We then use `n //= 10` to remove the last digit and repeat until all digits have been processed.

6. In the main function, `slow` starts at `n`, while `fast` starts at `sumOfSquares(n)`, so the fast pointer begins one transformation ahead of the slow pointer.

7. The variables `power` and `lam` are used to implement Brent’s cycle detection algorithm, a variation of Floyd’s method. `power` tracks the current block size, while `lam` counts how many steps the fast pointer has taken within that block.

8. While `slow != fast`, the algorithm checks whether `power == lam`. If they are equal, it moves `slow` to the current `fast` position, doubles `power`, and resets `lam` to zero.

9. During each iteration, `fast` advances by applying `sumOfSquares(fast)`, and `lam` increases by one. This process continues until the two pointers meet.

10. If the pointers meet at `1`, the sequence has reached the happy-number destination, so the function returns `True`.

11. If the pointers meet at a value other than `1`, a cycle has been detected that does not reach `1`, so the function returns `False`.

12. The key idea is that every number produces a deterministic next number through the sum-of-squares operation. Eventually, the sequence either reaches `1` or enters a cycle, and cycle detection distinguishes these cases without using a set.

13. The time complexity is `O(log n)` for each digit-square calculation initially, with the overall running time depending on the number of transformations before a cycle is detected. The auxiliary space complexity is `O(1)` because only a fixed number of variables are used.
"""