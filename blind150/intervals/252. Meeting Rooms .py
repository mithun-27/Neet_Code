#252. Meeting Rooms 
"""Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), determine if a person could add all meetings to their schedule without any conflicts. The intervals may be provided in any order.

Note: (0,8),(8,10) is not considered a conflict at 8

Example 1:

Input: intervals = [(0,30),(5,10),(15,20)]

Output: false
Explanation:

(0,30) and (5,10) will conflict
(0,30) and (15,20) will conflict
Example 2:

Input: intervals = [(5,8),(9,15)]

Output: true
Constraints:

0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000"""

#answer:
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]

            if i1.end > i2.start:
                return False
        return True


#example:
solution = Solution()
print(solution.canAttendMeetings([Interval(0,30), Interval(5,10), Interval(15,20)]))  # Output: False
print(solution.canAttendMeetings([Interval(5,8), Interval(9,15)]))  # Output: True
print(solution.canAttendMeetings([Interval(0,8), Interval(8,10)]))  # Output: True



"""
Walkthrough:
1. We are given a list of meeting intervals, and our goal is to determine whether a person can attend all meetings without any scheduling conflicts.
2. A conflict occurs when two meetings overlap in time, meaning one meeting starts before the previous meeting has ended.
3. To efficiently detect overlaps, we first sort all meetings based on their starting times.
4. After sorting, any potential overlap can only occur between neighboring meetings in the sorted order.
5. We then iterate through the meetings starting from the second meeting.
6. For each position, we compare the current meeting with the previous meeting.
7. Let:
   - `i1` be the previous meeting.
   - `i2` be the current meeting.
8. If:
   ```python
   i1.end > i2.start
then the previous meeting ends after the current meeting begins.
9. This means the two meetings overlap and cannot both be attended.
10. As soon as an overlap is found, we immediately return `False`.
11. If no overlap exists, we continue checking the remaining meetings.
12. If the loop completes successfully, it means every meeting starts after or exactly when the previous meeting ends.
13. Therefore, all meetings can be attended without any conflicts.
14. We then return `True`.
15. The key insight is that after sorting by start time, checking adjacent meetings is sufficient to detect every possible overlap.
16. The time complexity is `O(n log n)` because of sorting, and the overlap check takes `O(n)`.
17. The auxiliary space complexity is `O(1)` excluding the space used by the sorting algorithm.
"""