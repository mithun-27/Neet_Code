#57. Insert Interval
"""You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Two intervals are considered overlapping if they share at least one point.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105"""

#answer:
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
        res.append(newInterval)
        return res


#example:
"""Input
intervals =
[[1,3],[6,9]]
newInterval =
[2,5]
Output
[[1,5],[6,9]]
Expected
[[1,5],[6,9]]"""


"""Walkthrough:
1. We are given a list of non-overlapping intervals sorted by their start times and a new interval that must be inserted into the list.
2. Our goal is to insert the new interval while maintaining the sorted order and merging any overlapping intervals.
3. We create a result list `res` that will store the final set of intervals.
4. We iterate through each interval in the existing intervals list and compare it with the current `newInterval`.
5. If the end of `newInterval` is smaller than the start of the current interval, then `newInterval` comes completely before the current interval and does not overlap with it.
6. Since the intervals are already sorted, we can safely add `newInterval` to the result and return the result along with all remaining intervals.
7. If the start of `newInterval` is greater than the end of the current interval, then the current interval comes completely before `newInterval` and does not overlap with it.
8. In this case, we add the current interval to the result and continue checking the next intervals.
9. Otherwise, the current interval overlaps with `newInterval`.
10. When an overlap occurs, we merge them by updating:
    - The new start as the minimum of both starts.
    - The new end as the maximum of both ends.
11. After merging, `newInterval` now represents the combined interval and will continue to be compared with the remaining intervals.
12. This allows multiple overlapping intervals to be merged into a single larger interval.
13. We continue scanning the intervals until all intervals have been processed.
14. If the loop finishes without inserting `newInterval`, it means the merged interval belongs at the end of the list.
15. Therefore, we append the final version of `newInterval` to the result.
16. The result list now contains all intervals in sorted order with all necessary overlaps merged.
17. The key insight is that every interval falls into one of three cases: completely before the new interval, completely after the new interval, or overlapping with the new interval.
18. By handling these three cases in a single pass, we can efficiently build the final answer.
19. The time complexity is `O(n)` because each interval is processed once.
20. The auxiliary space complexity is `O(n)` for storing the resulting intervals."""