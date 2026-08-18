#743. Network Delay Time
"""You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

 

Example 1:


Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
 

Constraints:

1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All the pairs (ui, vi) are unique. (i.e., no multiple edges.)"""

#answer:
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        minHeap = [(0, k)]
        visit = set()
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = w1

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        return t if len(visit) == n else -1


#example 1 :
"""Input
times =
[[2,1,1],[2,3,1],[3,4,1]]
n =
4
k =
2
Output
2
Expected
2"""

#example 2 :
"""Input
times =
[[1,2,1]]
n =
2
k =
1
Output
1
Expected
1"""

#example 3 :
"""Input
times =
[[1,2,1]]
n =
2
k =
2
Output
-1
Expected
-1"""


"""Walkthrough:
1. We want to determine the minimum time required for a signal sent from node `k` to reach every node in the network. Since the graph has weighted directed edges, this is a shortest-path problem.
2. We use Dijkstra's Algorithm because all edge weights (travel times) are non-negative, making it efficient for finding the shortest distance from a source node to all other nodes.
3. We first build an adjacency list where each node stores its outgoing neighbors along with the travel time required to reach them.
4. We initialize a min-heap (priority queue) with the starting node `k` and a distance of `0`. The heap always gives us the node with the smallest known travel time.
5. We maintain a set of visited nodes. When a node is removed from the heap for the first time, we have found the shortest possible time needed to reach that node.
6. For the current node, we examine all of its outgoing edges. For each neighbor, we calculate the new travel time by adding the edge weight to the current node's shortest distance.
7. If the neighbor has not been finalized yet, we push the new distance and neighbor into the min-heap. The heap automatically prioritizes the path with the smallest travel time.
8. We continue processing nodes until the heap becomes empty. The last shortest distance processed represents the maximum time required for the signal to reach all reachable nodes.
9. If all `n` nodes have been visited, we return the maximum shortest distance found because that is the time when the final node receives the signal. Otherwise, some nodes are unreachable, so we return `-1`. The time complexity is `O((V + E) log V)` due to the priority queue operations, and the auxiliary space complexity is `O(V + E)` for the adjacency list, heap, and visited set."""