#435. Non Overlapping Intervals
"""Given an array of intervals intervals where intervals[i] = [start_i, end_i], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note: Intervals are non-overlapping even if they have a common point. For example, [1, 3] and [2, 4] are overlapping, but [1, 2] and [2, 3] are non-overlapping.

Example 1:

Input: intervals = [[1,2],[2,4],[1,4]]

Output: 1
Explanation: After [1,4] is removed, the rest of the intervals are non-overlapping.

Example 2:

Input: intervals = [[1,2],[2,4]]

Output: 0
Constraints:

1 <= intervals.length <= 100,000
intervals[i].length == 2
-50000 <= starti < endi <= 50000
"""

#answer:
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda pair: pair[1])
        prevEnd = intervals[0][1]
        res = 0

        for i in range(1, len(intervals)):
            if prevEnd > intervals[i][0]:
                res += 1
            else:
                prevEnd = intervals[i][1]


        return res

#example:
solution = Solution()
print(solution.eraseOverlapIntervals([[1,2],[2,4],[1,4]]))  # Output: 1
print(solution.eraseOverlapIntervals([[1,2],[2,4]]))  # Output: 0



#walkthrough:
"""Walkthrough:
1. We are given a collection of intervals and need to remove the minimum number of intervals so that the remaining intervals do not overlap.
2. A greedy strategy works best because we want to keep as many intervals as possible while removing as few as possible.
3. To maximize the number of intervals we can keep, we sort all intervals based on their ending times in ascending order.
4. Sorting by ending time ensures that we always choose the interval that finishes earliest, leaving the most room for future intervals.
5. After sorting, we assume the first interval is selected and store its ending value in `prevEnd`.
6. We also initialize a counter `res` to track the number of intervals that must be removed.
7. We then iterate through the remaining intervals one by one.
8. For each interval, we compare its start time with `prevEnd`, which represents the end of the last interval we decided to keep.
9. If the current interval starts before `prevEnd`, then it overlaps with the previously selected interval.
10. Since the intervals are sorted by ending time, the previously selected interval always ends earlier or at the same time.
11. Therefore, keeping the previous interval is always the better choice because it leaves more space for future intervals.
12. As a result, we remove the current interval and increment the removal counter:
    ```python
    res += 1
    ```
13. If the current interval starts at or after `prevEnd`, then there is no overlap.
14. In this case, we keep the current interval and update:
    ```python
    prevEnd = intervals[i][1]
    ```
15. This makes the current interval the latest interval included in our non-overlapping set.
16. We continue processing all intervals using the same logic.
17. By always keeping the interval with the earliest ending time among overlapping choices, we maximize the number of intervals that remain.
18. Consequently, the number of intervals removed is minimized.
19. After processing all intervals, `res` contains the minimum number of intervals that must be removed to eliminate all overlaps.
20. The time complexity is `O(n log n)` due to sorting, and the traversal itself takes `O(n)`.
21. The auxiliary space complexity is `O(1)` excluding the space used by the sorting algorithm."""