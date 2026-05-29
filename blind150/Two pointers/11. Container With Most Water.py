#11. Container With Most Water
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
    
#example:
height = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(height)) # Output: 49

"""walkthrough:
1. We initialize two pointers, l and r, to the beginning and end of the heights array, respectively.    
2. We also initialize a variable res to store the maximum area found so far.
3. We enter a while loop that continues until the two pointers meet.
4. Inside the loop, we calculate the area formed by the lines at the two pointers and the x-axis. The area is determined by the shorter line (the minimum of heights[l] and heights[r]) multiplied by the distance between the two pointers (r - l).
5. We update res with the maximum of the current area and the previously stored maximum area.
6. We then move the pointer that points to the shorter line inward, as this is the only way to potentially find a larger area. If heights[l] is less than or equal to heights[r], we move the left pointer right; otherwise, we move the right pointer left.
7. Finally, we return res, which contains the maximum area found.
8. The time complexity of this algorithm is O(n) since we traverse the heights array at most once, and the space complexity is O(1) as we only use a constant amount of extra space.    
9. This approach efficiently finds the maximum area without needing to check every possible pair of lines, which would have a time complexity of O(n^2).    """