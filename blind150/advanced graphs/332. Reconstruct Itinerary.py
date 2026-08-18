#332. Reconstruct Itinerary
"""You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

 

Example 1:


Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
Example 2:


Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
 

Constraints:

1 <= tickets.length <= 300
tickets[i].length == 2
fromi.length == 3
toi.length == 3
fromi and toi consist of uppercase English letters.
fromi != toi"""


#answer:
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)

        stack = ["JFK"]
        res = []

        while stack:
            curr = stack[-1]
            if not adj[curr]:
                res.append(stack.pop())
            else:
                stack.append(adj[curr].pop())

        return res[::-1]

#example 1 :
"""Input
tickets =
[["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output
["JFK","MUC","LHR","SFO","SJC"]
Expected
["JFK","MUC","LHR","SFO","SJC"]"""

#example 2 :
"""Input
tickets =
[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output
["JFK","ATL","JFK","SFO","ATL","SFO"]
Expected
["JFK","ATL","JFK","SFO","ATL","SFO"]"""


"""Walkthrough:
1. We want to reconstruct the complete flight itinerary using all tickets exactly once, starting from `"JFK"`. If multiple valid itineraries exist, we must return the one with the smallest lexical (alphabetical) order.
2. The tickets form a directed graph where each airport is a node and each ticket represents a directed edge from the source airport to the destination airport.
3. We first sort the tickets in reverse lexical order and build an adjacency list. By storing destinations in reverse order, we can efficiently retrieve the smallest lexical destination using `pop()`.
4. We use an iterative version of Hierholzer's Algorithm to find an Eulerian Path, since every ticket (edge) must be used exactly once.
5. We initialize a stack with `"JFK"` as the starting airport. The stack represents the current path being explored.
6. While the stack is not empty, we look at the airport on top of the stack. If it has any unused outgoing flights, we take the lexicographically smallest available destination and push it onto the stack.
7. If the current airport has no remaining outgoing flights, it means we have reached the end of a valid path. We remove it from the stack and add it to the result list.
8. This process continues until all tickets have been used and all airports have been added to the result. Since airports are added after exploring all outgoing edges, the result is built in reverse order.
9. Finally, we reverse the result list to obtain the correct itinerary. The time complexity is `O(E log E)` due to sorting the tickets, where `E` is the number of tickets. The traversal itself takes `O(E)`. The auxiliary space complexity is `O(E)` for the adjacency list, stack, and result list."""