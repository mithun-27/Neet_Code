#17. Letter Combinations of a Phone Number
"""Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

1 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9']."""


#answer
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = [""]
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        for digit in digits:
            tmp = []
            for curStr in res:
                for c in digitToChar[digit]:
                    tmp.append(curStr + c)
            res = tmp
        return res

"""Example 1:

Input: digits = "34"

Output: ["dg","dh","di","eg","eh","ei","fg","fh","fi"]
Example 2:

Input: digits = ""

Output: []"""

"""Walkthrough:
1. We want to generate all possible letter combinations represented by the given string of digits using the standard telephone keypad mapping.
2. We first create a mapping from each digit (`2`–`9`) to its corresponding letters. If the input string is empty, we return an empty list because there are no possible combinations.
3. We use a backtracking (depth-first search) approach to build each combination one letter at a time. The recursion keeps track of the current digit index and the current combination being formed.
4. At each recursive call, we look up the letters corresponding to the current digit and try each letter as the next character in the combination.
5. For every selected letter, we add it to the current combination and recursively move to the next digit in the input string.
6. If the current index reaches the length of the input string, it means we have selected one letter for every digit, so we add the completed combination to the result list.
7. After each recursive call, we backtrack by removing the last added letter. This allows us to explore all other possible letter choices for the current digit.
8. The algorithm continues until every possible combination has been generated exactly once. Since each digit contributes multiple choices, backtracking efficiently explores all valid combinations.
9. The time complexity is `O(4^n × n)` in the worst case, where `n` is the number of digits, because each digit can map to at most four letters and each generated combination has length `n`. The auxiliary space complexity is `O(n)` for the recursion stack and the current combination (excluding the output list)."""