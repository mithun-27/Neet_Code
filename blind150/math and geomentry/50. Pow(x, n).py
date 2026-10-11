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


"""Walkthrough:

1. We are given a floating-point number `x` and an integer `n`, and we need to calculate \\(x^n\\) efficiently without using a built-in power function.
2. We store `n` in a `long long` variable called `power` so that we can safely handle negative exponents, including the minimum integer value.
3. If `power` is negative, we convert the calculation using the mathematical rule \\(x^{-n} = \frac{1}{x^n}\\). Therefore, we replace `x` with `1 / x` and make `power` positive.
4. We initialize `res = 1.0` because multiplying by `1` does not change the result, making it the correct starting value for calculating the power.
5. We use Binary Exponentiation, also called Exponentiation by Squaring, which calculates powers by repeatedly squaring the base instead of multiplying it `n` times.
6. The algorithm continues while `power > 0`, processing the exponent one binary digit at a time.
7. Inside the loop, we check whether `power` is odd using `power % 2 == 1`. If it is odd, we multiply `res` by the current value of `x` because that power of the base must contribute to the final answer.
8. We then square the base using `x *= x`, which transforms \\(x\\) into \\(x^2\\), then \\(x^4\\), \\(x^8\\), and so on.
9. We divide `power` by `2` using `power /= 2`, discarding the processed binary digit and moving to the next exponent bit.
10. These steps repeat until `power` becomes `0`, at which point every required power has been incorporated into `res`.
11. Finally, we return `res`, which contains the calculated value of \\(x^n\\), including the reciprocal adjustment when the original exponent was negative.
12. The key idea is that each iteration squares the base and halves the exponent, reducing the number of iterations dramatically compared with ordinary multiplication.
13. The time complexity is \\(O(\log |n|)\\) because the exponent is halved during each iteration, and the auxiliary space complexity is \\(O(1)\\) because only a fixed number of variables are used."""