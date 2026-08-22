#787. Cheapest Flights Within K Stops
"""There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

 

Example 1:


Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
Example 2:


Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.
Example 3:


Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.
 

Constraints:

2 <= n <= 100
0 <= flights.length <= (n * (n - 1) / 2)
flights[i].length == 3
0 <= fromi, toi < n
fromi != toi
1 <= pricei <= 104
There will not be any multiple flights between two cities.
0 <= src, dst, k < n
src != dst"""

#answer :
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        adj = [[] for _ in range(n)]
        for u, v, cst in flights:
            adj[u].append([v, cst])

        q = deque([(0, src, 0)])
        while q:
            cst, node, stops = q.popleft()
            if stops > k:
                continue

            for nei, w in adj[node]:
                nextCost = cst + w
                if nextCost < prices[nei]:
                    prices[nei] = nextCost
                    q.append((nextCost, nei, stops + 1))

        return prices[dst] if prices[dst] != float("inf") else -1


#example 1:
"""Input
n =
4
flights =
[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src =
0
dst =
3
k =
1
Output
700
Expected
700"""

#example 2:
"""Input
n =
3
flights =
[[0,1,100],[1,2,100],[0,2,500]]
src =
0
dst =
2
k =
1
Output
200
Expected
200"""


#walkthrough:
"""
1. We want to find the cheapest price from `src` to `dst` while using at most `k` stops. Since a path with more stops may be cheaper, a normal shortest-path algorithm cannot be used directly without considering the stop limit.
2. We use a modified Bellman-Ford Algorithm because it naturally handles paths with a limited number of edges. If we are allowed `k` stops, then the route can contain at most `k + 1` flights.
3. We initialize a distance array where `dist[src] = 0` and all other cities are assigned infinity, representing that they are initially unreachable.
4. We perform exactly `k + 1` relaxation rounds. Each round represents allowing one more flight in the path.
5. At the start of each round, we create a copy of the current distance array. This prevents updates made during the current round from affecting other relaxations within the same round.
6. We iterate through every flight `[from, to, price]`. If the source city of the flight is reachable, we attempt to improve the cost of reaching the destination city using that flight.
7. If `dist[from] + price` is smaller than the current recorded cost for `to`, we update the copied distance array with the cheaper value.
8. After processing all flights in a round, we replace the original distance array with the updated copy. This ensures that only paths using up to the allowed number of flights are considered.
9. After completing all `k + 1` rounds, the value of `dist[dst]` represents the cheapest valid route. If it is still infinity, no route exists within the stop limit, so we return `-1`. The time complexity is `O((k + 1) × E)`, where `E` is the number of flights, and the auxiliary space complexity is `O(n)` for the distance arrays."""