#55. Jump Game
"""You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105"""

#answer:
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0


#example:
"""Input
nums =
[2,3,1,1,4]
Output
true
Expected
true
"""

#example:
"""Input
nums =
[3,2,1,0,4]
Output
false
Expected
false
"""

"""Walkthrough:
1. We want to determine whether we can reach the last index of the array starting from index `0`, where each element represents the maximum jump length from that position.
2. Instead of exploring all possible jumps using recursion or dynamic programming, we use a greedy approach that works backward from the end of the array.
3. We maintain a variable called `goal`, which represents the leftmost position that must be reached in order to eventually reach the last index.
4. Initially, the last index is our goal because reaching it means we have successfully completed the task.
5. We traverse the array from right to left, starting from the second-last index and moving toward the beginning.
6. At each index `i`, we check whether the maximum jump from that position can reach the current goal position.
7. If `i + nums[i]` is greater than or equal to the current goal, then index `i` can reach the goal.
8. Since index `i` can reach the goal, we update the goal to `i`, making it the new position that must be reached.
9. We continue this process for every index, repeatedly moving the goal closer to the beginning of the array whenever possible.
10. By the end of the traversal, the goal represents the leftmost index from which the last index is reachable.
11. If the goal becomes `0`, it means the starting position can eventually reach the last index, so we return `True`.
12. If the goal is not `0`, then there is no sequence of jumps that allows us to reach the last index, so we return `False`.
13. The key insight is that instead of asking "Can I reach the end from here?", we repeatedly ask "Can this position reach the current goal?" and move the goal backward whenever the answer is yes.
14. This greedy strategy guarantees the correct answer because every updated goal represents a position that can successfully lead to the end of the array.
15. The time complexity is `O(n)` since we scan the array only once, and the auxiliary space complexity is `O(1)` because only a single variable is used."""