#50. Pow(x, n)
"""Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
Either x is not zero or n > 0.
-104 <= xn <= 104"""

#answer:

class Solution {
public:
    double myPow(double x, int n) {
        long long power = n;

        if (power < 0) {
            x = 1 / x;
            power = -power;
        }

        double res = 1.0;

        while (power > 0) {
            if (power % 2 == 1) {
                res *= x;
            }

            x *= x;
            power /= 2;
        }

        return res;
    }
};


#example:
s = Solution()
print(s.myPow(2.00000, 10))  # Output: 1024.00000
print(s.myPow(2.10000, 3))   # Output: 9.26100
print(s.myPow(2.00000, -2))  # Output: 0.25000