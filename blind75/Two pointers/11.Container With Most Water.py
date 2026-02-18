#11.Container With Most Water

"""You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104"""

#answer
from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res
    
#example usage
solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))  # Output: 49
print(solution.maxArea([1,1]))  # Output: 1

"""walkthrough the code:
1. We initialize two pointers, `l` and `r`, to the start and end of the `heights` array, respectively. We also initialize a variable `res` to store the maximum area found. 
2. We enter a while loop that continues until the two pointers meet. Inside the loop, we calculate the area formed by the lines at the `l` and `r` pointers, which is the minimum of the two heights multiplied by the distance between them (r - l). We update `res` if this area is greater than the current maximum.
3. We then move the pointer that points to the shorter line inward, as this is the only way to potentially find a larger area. If the height at `l` is less than or equal to the height at `r`, we move `l` to the right; otherwise, we move `r` to the left.
4. Once the pointers meet, we exit the loop and return the maximum area found in `res`.
This approach efficiently finds the maximum area in O(n) time, where n is the length of the `heights` array, since we are only traversing the array once with the two pointers.
"""