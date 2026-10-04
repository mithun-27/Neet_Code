#1851. Minimum Interval to Include Each Query
"""You are given a 2D integer array intervals, where intervals[i] = [lefti, righti] describes the ith interval starting at lefti and ending at righti (inclusive). The size of an interval is defined as the number of integers it contains, or more formally righti - lefti + 1.

You are also given an integer array queries. The answer to the jth query is the size of the smallest interval i such that lefti <= queries[j] <= righti. If no such interval exists, the answer is -1.

Return an array containing the answers to the queries.

 

Example 1:

Input: intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
Output: [3,3,1,4]
Explanation: The queries are processed as follows:
- Query = 2: The interval [2,4] is the smallest interval containing 2. The answer is 4 - 2 + 1 = 3.
- Query = 3: The interval [2,4] is the smallest interval containing 3. The answer is 4 - 2 + 1 = 3.
- Query = 4: The interval [4,4] is the smallest interval containing 4. The answer is 4 - 4 + 1 = 1.
- Query = 5: The interval [3,6] is the smallest interval containing 5. The answer is 6 - 3 + 1 = 4.
Example 2:

Input: intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
Output: [2,-1,4,6]
Explanation: The queries are processed as follows:
- Query = 2: The interval [2,3] is the smallest interval containing 2. The answer is 3 - 2 + 1 = 2.
- Query = 19: None of the intervals contain 19. The answer is -1.
- Query = 5: The interval [2,5] is the smallest interval containing 5. The answer is 5 - 2 + 1 = 4.
- Query = 22: The interval [20,25] is the smallest interval containing 22. The answer is 25 - 20 + 1 = 6.
 

Constraints:

1 <= intervals.length <= 105
1 <= queries.length <= 105
intervals[i].length == 2
1 <= lefti <= righti <= 107
1 <= queries[j] <= 107"""

#answer:
class SegmentTree:
    def __init__(self, N):
        self.n = N
        self.tree = [float('inf')] * (4 * N)
        self.lazy = [float('inf')] * (4 * N)

    def propagate(self, treeidx, lo, hi):
        if self.lazy[treeidx] != float('inf'):
            self.tree[treeidx] = min(self.tree[treeidx], self.lazy[treeidx])
            if lo != hi:
                self.lazy[2 * treeidx + 1] = min(self.lazy[2 * treeidx + 1], self.lazy[treeidx])
                self.lazy[2 * treeidx + 2] = min(self.lazy[2 * treeidx + 2], self.lazy[treeidx])
            self.lazy[treeidx] = float('inf')

    def update(self, treeidx, lo, hi, left, right, val):
        self.propagate(treeidx, lo, hi)
        if lo > right or hi < left:
            return
        if lo >= left and hi <= right:
            self.lazy[treeidx] = min(self.lazy[treeidx], val)
            self.propagate(treeidx, lo, hi)
            return
        mid = (lo + hi) // 2
        self.update(2 * treeidx + 1, lo, mid, left, right, val)
        self.update(2 * treeidx + 2, mid + 1, hi, left, right, val)
        self.tree[treeidx] = min(self.tree[2 * treeidx + 1], self.tree[2 * treeidx + 2])

    def query(self, treeidx, lo, hi, idx):
        self.propagate(treeidx, lo, hi)
        if lo == hi:
            return self.tree[treeidx]
        mid = (lo + hi) // 2
        if idx <= mid:
            return self.query(2 * treeidx + 1, lo, mid, idx)
        else:
            return self.query(2 * treeidx + 2, mid + 1, hi, idx)

    def update_range(self, left, right, val):
        self.update(0, 0, self.n - 1, left, right, val)

    def query_point(self, idx):
        return self.query(0, 0, self.n - 1, idx)

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        points = []
        for interval in intervals:
            points.append(interval[0])
            points.append(interval[1])
        for q in queries:
            points.append(q)

        # Compress the coordinates
        points = sorted(set(points))
        compress = {points[i]: i for i in range(len(points))}

        # Lazy Segment Tree
        segTree = SegmentTree(len(points))

        for interval in intervals:
            start = compress[interval[0]]
            end = compress[interval[1]]
            length = interval[1] - interval[0] + 1
            segTree.update_range(start, end, length)

        ans = []
        for q in queries:
            idx = compress[q]

            # query for minSize
            res = segTree.query_point(idx)
            ans.append(res if res != float('inf') else -1)
        return ans


#example:
solution = Solution()
print(solution.minInterval([[1,4],[2,4],[3,6],[4,4]], [2,3,4,5]))  # Output: [3,3,1,4]
print(solution.minInterval([[2,3],[2,5],[1,8],[20,25]], [2,19,5,22]))  # Output: [2,-1,4,6] 
print(solution.minInterval([[1,2],[3,4],[5,6]], [7,8,9]))  # Output: [-1,-1,-1]


"""Walkthrough:
1. We are given several intervals and queries, and for each query we need to find the size of the smallest interval that contains that query.
2. Since interval values and query values can be large, we first collect every interval start, interval end, and query value into a single list called `points`.
3. We sort these values, remove duplicates, and perform coordinate compression so that each original value is mapped to a smaller index from `0` to `N - 1`.
4. After compression, every interval `[left, right]` becomes a range of compressed indices, which allows us to process it efficiently using a Segment Tree.
5. The Segment Tree is initialized with `infinity` because initially no interval has been assigned to any position.
6. Each tree node stores the minimum interval size that covers its range, and the `lazy` array stores pending minimum updates that still need to be pushed to child nodes.
7. For every original interval, we calculate its size using:
   `length = right - left + 1`.
8. We then update the compressed range corresponding to that interval with this length.
9. The update operation is a range-min update, meaning every compressed point inside the interval should remember the smallest interval length that covers it.
10. Before accessing a Segment Tree node, `propagate()` applies any pending lazy value to that node using `min()`.
11. If the current Segment Tree range is completely outside the update range, we ignore it.
12. If the current range is completely inside the interval range, we store the minimum interval length in the lazy value and propagate it immediately.
13. If the current range only partially overlaps, we recursively update both children and then store the minimum value of the two children in the current node.
14. After all intervals have been added to the Segment Tree, each compressed position can tell us the minimum interval size that covers that point.
15. For every query, we convert the query value into its compressed index.
16. We then perform a point query on the Segment Tree to find the minimum interval size stored at that position.
17. During the point query, pending lazy updates are propagated while moving from the root toward the corresponding leaf node.
18. Once we reach the leaf representing the query position, its value gives the size of the smallest interval containing that query.
19. If the value is still `infinity`, then no interval contains that query, so we return `-1`.
20. Otherwise, we add the minimum interval size to the answer list.
21. After processing every query, we return the complete answer list.
22. The key idea is to combine coordinate compression with a lazy Segment Tree so that each interval performs a range minimum update and each query performs a point lookup.
23. If `N` is the number of unique compressed coordinates, each range update takes `O(log N)` in typical Segment Tree analysis and each point query takes `O(log N)`.
24. Therefore, the overall complexity is roughly `O((I + Q) log N + N log N)` including coordinate sorting, where `I` is the number of intervals and `Q` is the number of queries.
25. The auxiliary space complexity is `O(N)` for the compressed coordinates, mapping, Segment Tree, and lazy array."""