#239. Sliding Window Maximum
"""You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length"""

#answer
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # index
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output

#example 1:
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(Solution().maxSlidingWindow(nums, k)) # Output: [3,3,5,5,6,7]
#example 2:
nums = [1]
k = 1
print(Solution().maxSlidingWindow(nums, k)) # Output: [1]

"""walkthrough:
1. We initialize an empty list output to store the maximum values of each sliding window, and a deque q to keep track of the indices of the elements in the current window. We also initialize two pointers l and r to represent the left and right boundaries of the sliding window.
2. We iterate through the nums array using the right pointer r. For each element at index r, we check if there are any indices in the deque q whose corresponding values in nums are less than the current element. If there are, we pop those indices from the deque since they cannot be the maximum for the current or future windows.
3. We then append the current index r to the deque q.
4. Next, we check if the left pointer l is greater than the index at the front of the deque q. If it is, it means that the maximum element for the current window has moved out of the window, so we pop it from the front of the deque.
5. We then check if the current window size (r + 1) is greater than or equal to k. If it is, we append the value at the index at the front of the deque q to the output list, since that index corresponds to the maximum element in the current window. We also increment the left pointer l to move the window to the right.
6. Finally, we return the output list containing the maximum values for each sliding window.
"""