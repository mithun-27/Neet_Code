#253. Meeting Rooms II
"""Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of rooms required to schedule all meetings without any conflicts.

Note: (0,8),(8,10) is NOT considered a conflict at 8.

Example 1:

Input: intervals = [(0,40),(5,10),(15,20)]

Output: 2
Explanation:
room1: (0,40)
room2: (5,10),(15,20)

Example 2:

Input: intervals = [(4,9)]

Output: 1
Constraints:

0 <= intervals.length <= 100,000
0 <= intervals[i].start < intervals[i].end <= 1,000,000"""


#answer:
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

from annotated_types import Interval


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        time = []
        for i in intervals:
            time.append((i.start, 1))
            time.append((i.end, -1))

        time.sort(key=lambda x: (x[0], x[1]))

        res = count = 0
        for t in time:
            count += t[1]
            res = max(res, count)
        return res


#example:
solution = Solution()
print(solution.minMeetingRooms([Interval(0,40), Interval(5,10), Interval(15,20)]))  # Output: 2
print(solution.minMeetingRooms([Interval(4,9)]))  # Output: 1   


"""Walkthrough:
1. We are given a list of meeting intervals and need to determine the minimum number of meeting rooms required so that all meetings can be conducted without conflicts.
2. The key observation is that the number of rooms needed at any moment equals the number of meetings occurring simultaneously.
3. To track this efficiently, we use a sweep-line approach that processes meeting start and end events in chronological order.
4. For every meeting interval, we create two events:
   - `(start, 1)` representing a meeting starting.
   - `(end, -1)` representing a meeting ending.
5. These events are stored in a list called `time`.
6. After collecting all events, we sort them by time.
7. If two events occur at the same time, ending events (`-1`) are processed before starting events (`1`).
8. This ordering is important because a room freed by an ending meeting can immediately be reused by a meeting starting at the same time.
9. We maintain a variable `count` to represent the number of meeting rooms currently in use.
10. We also maintain `res` to store the maximum number of rooms used at any point.
11. We process each event in sorted order.
12. When we encounter a start event `(time, 1)`, we increase `count` because a new room is being occupied.
13. When we encounter an end event `(time, -1)`, we decrease `count` because a room becomes available.
14. After updating `count`, we update:
    ```python
    res = max(res, count)
    ```
15. This ensures that `res` always stores the highest number of simultaneously active meetings seen so far.
16. By the end of the traversal, `res` represents the maximum overlap among all meetings.
17. Since each overlapping meeting requires its own room, this maximum overlap is exactly the minimum number of meeting rooms required.
18. The key insight is that meeting starts increase room demand while meeting ends decrease room demand, and the peak demand determines the answer.
19. The time complexity is `O(n log n)` because we sort `2n` events.
20. The auxiliary space complexity is `O(n)` because we store all start and end events."""