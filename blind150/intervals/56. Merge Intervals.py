#56. Merge Intervals
"""Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
Example 3:

Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
Example 3:

Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104"""


#answer:
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        max_val = max(interval[0] for interval in intervals)

        mp = [0] * (max_val + 1)
        for start, end in intervals:
            mp[start] = max(end + 1, mp[start])

        res = []
        have = -1
        interval_start = -1
        for i in range(len(mp)):
            if mp[i] != 0:
                if interval_start == -1:
                    interval_start = i
                have = max(mp[i] - 1, have)
            if have == i:
                res.append([interval_start, have])
                have = -1
                interval_start = -1

        if interval_start != -1:
            res.append([interval_start, have])

        return res


#example:
"""Input
intervals =
[[1,3],[2,6],[8,10],[15,18]]
Output
[[1,6],[8,10],[15,18]]
Expected
[[1,6],[8,10],[15,18]]"""

"""Walkthrough:
1. We are given a collection of intervals, and our goal is to merge all overlapping intervals so that the final result contains only non-overlapping intervals covering the same ranges.
2. Instead of sorting the intervals by their starting positions, this solution creates a mapping structure that records interval information directly based on their start values.
3. We first determine the largest starting value among all intervals because this tells us how large the mapping array must be.
4. We create an array called `mp` where each index represents a possible interval start position.
5. For every interval `[start, end]`, we store the farthest ending position associated with that start index.
6. If multiple intervals start at the same position, we keep only the interval with the largest ending value because it completely covers the shorter ones.
7. The value stored in `mp[start]` is `end + 1`, which helps distinguish valid entries from unused positions initialized with zero.
8. After constructing the mapping array, we scan it from left to right to build merged intervals.
9. We maintain two variables: `interval_start`, which stores the beginning of the current merged interval, and `have`, which stores the farthest ending position currently reachable.
10. Whenever we encounter a non-zero entry in the mapping array, it means an interval begins at that position.
11. If no merged interval is currently active, we start a new merged interval at the current index.
12. We then update `have` to be the maximum between its current value and the ending position stored at this index.
13. This step effectively extends the active interval whenever another overlapping interval reaches farther to the right.
14. As we continue scanning, every interval whose starting position lies before the current boundary automatically becomes part of the same merged interval.
15. The variable `have` therefore represents the farthest point that the current merged interval can reach.
16. Whenever the current index becomes equal to `have`, it means there are no more intervals capable of extending the current merged range.
17. At this moment, we have identified a complete merged interval from `interval_start` to `have`.
18. We add this interval to the result list and reset the tracking variables to begin searching for the next merged interval.
19. The scan then continues until every position in the mapping array has been processed.
20. If a merged interval is still active after the loop finishes, it is added to the result as the final interval.
21. The final result contains all overlapping intervals merged together and all non-overlapping intervals preserved.
22. The key idea is that the mapping array allows us to track the farthest reachable endpoint from every start position and continuously expand intervals while scanning from left to right.
23. This approach avoids explicit interval sorting and instead reconstructs merged intervals directly from the start-position mapping.
24. The time complexity is `O(M + n)`, where `M` is the maximum interval start value and `n` is the number of intervals.
25. The auxiliary space complexity is `O(M)` because the mapping array stores information for every possible start position up to the maximum start value."""