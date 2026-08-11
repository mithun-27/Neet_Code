#207. Course Schedule
"""There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique."""


#answer:
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for src, dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)

        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        finish = 0
        while q:
            node = q.popleft()
            finish += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return finish == numCourses

#example 1 :
"""Input
numCourses =
2
prerequisites =
[[1,0]]
Output
true
Expected
true
"""

#example 2 :
"""Input
numCourses =
2
prerequisites =
[[1,0],[0,1]]
Output
false
Expected
false
"""

"""Walkthrough:
1. We want to determine whether it is possible to finish all courses while satisfying every prerequisite. This can be represented as a directed graph where each course is a node and each prerequisite creates an edge from the prerequisite course to the course that depends on it.
2. We use Topological Sort with Breadth-First Search (BFS) to determine whether the graph contains a cycle.
3. We first build an adjacency list where `graph[bi]` contains all courses that can be taken after completing course `bi`. At the same time, we calculate the indegree of every course, which represents the number of prerequisites it still has.
4. We find all courses with an indegree of `0`. These courses have no remaining prerequisites, so they can be taken immediately. We add them to a queue.
5. We process the queue using BFS. Whenever we complete a course, we reduce the indegree of all courses that depend on it because one of their prerequisites has now been completed.
6. If the indegree of a neighboring course becomes `0`, all of its prerequisites have been completed, so we add that course to the queue.
7. We keep a count of how many courses have been successfully processed. If all `numCourses` courses are processed, it means there is a valid ordering of courses and we return `True`.
8. If some courses cannot be processed, their prerequisites form a cycle. For example, `[1,0]` and `[0,1]` create a cycle where course `0` requires course `1` and course `1` requires course `0`, so we return `False`.
9. The time complexity is `O(V + E)`, where `V` is the number of courses and `E` is the number of prerequisites, because every course and prerequisite relationship is processed at most once. The auxiliary space complexity is `O(V + E)` for the adjacency list, indegree array, and BFS queue."""