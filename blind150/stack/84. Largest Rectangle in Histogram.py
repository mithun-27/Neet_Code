#84. Largest Rectangle in Histogram
"""Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4
 

Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104"""

#answer
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        stack = []

        for i in range(n + 1):
            while stack and (i == n  or heights[stack[-1]] >= heights[i]):
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, height * width)
            stack.append(i)
        return maxArea
    
#example 1:
"""Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3] 
Output: 3  """ 
#example 2:
"""Input: target = 10, position = [3], speed = [3]  
Output: 1  """
#example 3:
"""Input: target = 100, position = [0,2,4], speed = [4,2,1] 
Output: 1  """

"""walkthrough:
1. We initialize an empty stack to keep track of the indices of the histogram bars and a variable maxArea to store the maximum area found.
2. We iterate through the histogram bars using a loop that goes from 0 to n (the length of the heights array). We also include an extra iteration (i == n) to handle the case when we reach the end of the histogram.
3. Inside the loop, we check if the stack is not empty and if the current bar is shorter than the bar at the top of the stack. If this condition is true, it means we have found a right boundary for the bar at the top of the stack. We pop the index from the stack and calculate the height of the rectangle using the height of the bar at that index. We also calculate the width of the rectangle, which is the distance between the current index and the index of the new top of the stack (after popping). If the stack is empty after popping, it means the rectangle extends all the way to the left, so the width is simply the current index (i). We then calculate the area of the rectangle and update maxArea if the calculated area is larger.
4 . After processing all bars, we return the maxArea found. 
This algorithm efficiently computes the largest rectangle in the histogram with a time complexity of O(n) and a space complexity of O(n) due to the stack.          
"""