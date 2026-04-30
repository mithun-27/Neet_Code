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

0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000
"""

#answer
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

from sqlalchemy import Interval


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
    
#example
intervals = [Interval(0,40), Interval(5,10), Interval(15,20)]
s = Solution()
print(s.minMeetingRooms(intervals))

"""walkthrough:
1. We create a list called `time` to store the start and end times of the meetings. For each meeting interval, we add a tuple (start time, 1) to indicate the start of a meeting and a tuple (end time, -1) to indicate the end of a meeting.       
2. We sort the `time` list first by the time value and then by the type of event (start or end). This ensures that if two events have the same time, the start event will be processed before the end event, which is crucial for accurately counting the number of ongoing meetings.   
3. We initialize two variables, `res` to keep track of the maximum number of rooms needed and `count` to count the current number of ongoing meetings. We iterate through the sorted `time` list, updating the `count` based on whether we encounter a start or end event. After updating the count for each event, we update `res` to be the maximum of its current value and the updated count.   
4. Finally, we return `res`, which represents the minimum number of rooms required to schedule all meetings without any conflicts.  
This approach efficiently counts the number of overlapping meetings at any given time, allowing us to determine the minimum number of rooms needed. The time complexity of this solution is O(n log n) due to the sorting step, and the space complexity is O(n) for storing the start and end times in the `time` list.    
"""