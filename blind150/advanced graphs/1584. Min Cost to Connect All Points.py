#1584. Min Cost to Connect All Points
"""You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

 

Example 1:


Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation: 

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
Example 2:

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
 

Constraints:

1 <= points.length <= 1000
-106 <= xi, yi <= 106
All pairs (xi, yi) are distinct."""

#answer:
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n, node = len(points), 0
        dist = [100000000] * n
        visit = [False] * n
        edges, res = 0, 0

        while edges < n - 1:
            visit[node] = True
            nextNode = -1
            for i in range(n):
                if visit[i]:
                    continue
                curDist = (abs(points[i][0] - points[node][0]) +
                           abs(points[i][1] - points[node][1]))
                dist[i] = min(dist[i], curDist)
                if nextNode == -1 or dist[i] < dist[nextNode]:
                    nextNode = i

            res += dist[nextNode]
            node = nextNode
            edges += 1

        return res

#example 1:
"""Input
points =
[[0,0],[2,2],[3,10],[5,2],[7,0]]
Output
20
Expected
20
"""

#example 2:
"""Input
points =
[[3,12],[-2,5],[-4,1]]
Output
18
Expected
18"""

"""Walkthrough:
1. We want to connect all given points with the minimum possible total cost, where the cost between two points is their Manhattan distance. Since every point must be connected with exactly one simple path between any two points, we are looking for a Minimum Spanning Tree (MST).
2. We can solve this problem using Prim's Algorithm, which gradually builds the MST by always selecting the cheapest edge that connects a new point to the existing connected component.
3. We start with any point (usually point `0`) and mark it as visited. This point becomes the initial part of the MST.
4. For every unvisited point, we calculate its Manhattan distance from the current point and add the pair `(cost, point)` to a min-heap (priority queue).
5. The min-heap always stores the cheapest available edges. We repeatedly remove the edge with the smallest cost from the heap.
6. If the destination point of that edge has already been visited, we ignore it because adding it would create a cycle. Otherwise, we add the point to the MST and include the edge cost in the total answer.
7. After adding a new point, we compute its Manhattan distance to all remaining unvisited points and push those edges into the min-heap. This ensures that the heap always contains all possible ways to expand the MST.
8. We continue this process until all points have been visited. At that moment, every point belongs to a single connected component, and the selected edges form a valid minimum spanning tree.
9. The accumulated cost is the minimum cost required to connect all points. The time complexity is `O(n² log n)` because distances to other points are inserted into the heap during the MST construction, and the auxiliary space complexity is `O(n²)` for the heap and distance information in the worst case."""