#435. Non-overlapping Intervals
"""Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

 

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

Constraints:

1 <= intervals.length <= 105
intervals[i].length == 2
-5 * 104 <= starti < endi <= 5 * 104"""


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
"""Input
intervals =
[[1,2],[2,3],[3,4],[1,3]]
Output
1
Expected
1"""

#example:
"""Input
intervals =
[[1,2],[1,2],[1,2]]
Output
2
Expected
2"""


"""Walkthrough:
1. We are given a set of intervals and need to remove the minimum number of intervals so that the remaining intervals do not overlap.
2. A greedy strategy works best because at every step we want to keep the interval that leaves the most room for future intervals.
3. To achieve this, we first sort all intervals based on their ending times in ascending order.
4. After sorting, the interval that ends earliest appears first, making it the safest interval to keep.
5. We initialize `prevEnd` with the ending time of the first interval because we always keep the earliest-ending interval initially.
6. We also maintain a variable `res` to count the number of intervals that must be removed.
7. We then iterate through the remaining intervals one by one.
8. For each interval, we compare its start time with `prevEnd`, which represents the end of the last interval that was kept.
9. If the current interval starts before `prevEnd`, an overlap exists because the previous kept interval has not finished yet.
10. Since the intervals are sorted by ending time, the previously kept interval ends earlier than the current interval.
11. Therefore, keeping the previous interval is always the better choice because it leaves more space for future intervals.
12. As a result, we remove the current interval and increment the removal count `res`.
13. In this case, we do not update `prevEnd` because the previous interval remains the interval we are keeping.
14. If the current interval starts at or after `prevEnd`, there is no overlap.
15. We can safely keep the current interval and update `prevEnd` to its ending time.
16. This process continues until all intervals have been examined.
17. By always keeping the interval with the earliest ending time whenever an overlap occurs, we maximize the number of intervals that can remain.
18. Since minimizing removals is equivalent to maximizing the number of non-overlapping intervals kept, this greedy strategy produces the optimal answer.
19. After processing all intervals, `res` contains the minimum number of intervals that must be removed.
20. The time complexity is `O(n log n)` due to sorting, and the auxiliary space complexity is `O(1)` excluding the sorting space."""