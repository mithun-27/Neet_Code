#155. Min Stack
"""Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int value) pushes the element value onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin."""

#answer
class MinStack:
    def __init__(self):
        self.min = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val

    def pop(self) -> None:
        if not self.stack:
            return

        pop = self.stack.pop()

        if pop < 0:
            self.min = self.min - pop

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min

    def getMin(self) -> int:
        return self.min
    
#example 1:
minStack = MinStack()   
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin()) # return -3
minStack.pop()
print(minStack.top())    # return 0
print(minStack.getMin()) # return -2
print(minStack.stack) 

"""walkthrough:
1. We initialize the stack and set the minimum value to positive infinity.
2. When we push a value onto the stack, we check if the stack is empty. If it is, we simply push 0 onto the stack and set the minimum value to the pushed value. If the stack is not empty, we push the difference between the pushed value and the current minimum value onto the stack. If the pushed value is less than the current minimum value, we update the minimum value to the pushed value.
3. When we pop a value from the stack, we check if the popped value is negative. If it is, it means that the popped value was the minimum value at the time it was pushed, so we update the minimum value by subtracting the popped value from the current minimum value.
4. When we get the top value of the stack, we check if the top value is positive. If it is, we return the sum of the top value and the current minimum value. If it is negative, it means that the top value is the minimum value, so we return the current minimum value.
5. When we get the minimum value, we simply return the current minimum value.   
This implementation allows us to perform all operations in constant time while keeping track of the minimum value efficiently.  
"""