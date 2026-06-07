#150. Evaluate Reverse Polish Notation
"""You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
 

Constraints:

1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200]."""

#answer
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
        return stack[0]
    
#example 1:
#Input: tokens = ["2","1","+","3","*"]
#Output: 9
#Explanation: ((2 + 1) * 3) = 9
#example 2:
#Input: tokens = ["4","13","5","/","+"] 
#Output: 6
#Explanation: (4 + (13 / 5)) = 6    
#example 3:
#Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
#Output: 22
#Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
#= ((10 * (6 / (12 * -11))) + 17) + 5
#= ((10 * (6 / -132)) + 17) + 5 
#= ((10 * 0) + 17) + 5
#= (0 + 17) + 5 
#= 17 + 5
#= 22

"""walkthrough:
1. We initialize an empty stack to store the operands.
2. We iterate through each token in the input list:
   - If the token is an operator ("+", "-", "*", "/"), we pop the top two operands from the stack, perform the corresponding operation, and push the result back onto the stack.
   - If the token is an integer, we convert it to an integer and push it onto the stack.
3. After processing all tokens, the final result will be the only remaining element in the stack, which we return.  
The time complexity of this solution is O(n), where n is the number of tokens in the input list, since we process each token once. The space complexity is O(n) in the worst case, if all tokens are operands and we push them onto the stack. However, in practice, the space used will be less than n due to the presence of operators that reduce the number of operands on the stack.   
This solution correctly handles the order of operations and the division truncation towards zero as specified in the problem statement. The use of a stack allows us to easily manage the operands and operators as we evaluate the expression in Reverse Polish Notation.  
"""