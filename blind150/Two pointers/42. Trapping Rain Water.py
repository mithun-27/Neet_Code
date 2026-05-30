#42. Trapping Rain Water
"""Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105"""

#answer
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
    
#example 1:
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution().trap(height)) # Output: 6
#example 2:
height = [4,2,0,3,2,5]
print(Solution().trap(height)) # Output: 9

"""walkthrough:
1. We initialize two pointers, l and r, to the beginning and end of the height array, respectively. We also initialize leftMax and rightMax to the heights at these pointers, and a variable res to store the total amount of trapped water.    
2. We enter a while loop that continues until the two pointers meet.
3. Inside the loop, we compare leftMax and rightMax. If leftMax is less than rightMax, it means that the amount of water trapped at the left pointer is limited by leftMax. We move the left pointer to the right, update leftMax if necessary, and add the difference between leftMax and the current height at the left pointer to res.   
4. If rightMax is less than or equal to leftMax, it means that the amount of water trapped at the right pointer is limited by rightMax. We move the right pointer to the left, update rightMax if necessary, and add the difference between rightMax and the current height at the right pointer to res.    
5. Finally, we return res, which contains the total amount of trapped water.
6. The time complexity of this algorithm is O(n) since we traverse the height array at most once, and the space complexity is O(1) as we only use a constant amount of extra space.
7. This approach efficiently calculates the trapped water without needing to check every possible pair of bars, which would have a time complexity of O(n^2).    """    