#210. Course Schedule II
"""There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct."""

#answer:
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        indegree = [0] * numCourses
        for nxt, pre in prerequisites:
            indegree[nxt] += 1
            adj[pre].append(nxt)

        output = []

        def dfs(node):
            output.append(node)
            indegree[node] -= 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    dfs(nei)

        for i in range(numCourses):
            if indegree[i] == 0:
                dfs(i)

        return output if len(output) == numCourses else []


#example 1 :
"""Input
numCourses =
2
prerequisites =
[[1,0]]
Output
[0,1]
Expected
[0,1]
"""

#example 2 :
"""Input
numCourses =
4
prerequisites =
[[1,0],[2,0],[3,1],[3,2]]
Output
[0,1,2,3]
Expected
[0,2,1,3]"""

#example 3 :
"""Input
numCourses =
1
prerequisites =
[]
Output
[0]
Expected
[0]"""


"""Walkthrough:
1. We want to find a valid ordering of all courses such that every prerequisite course is completed before the course that depends on it. This can be represented as a directed graph.
2. We use Topological Sort with Breadth-First Search (BFS). Each course is a node, and a prerequisite relationship `[a, b]` creates an edge from course `b` to course `a`.
3. We first build an adjacency list where `graph[b]` contains the courses that can be taken after completing course `b`. At the same time, we calculate the indegree of every course, which represents how many prerequisites are still remaining for that course.
4. We find all courses with an indegree of `0`. These courses have no prerequisites, so they can be taken immediately, and we add them to the queue.
5. We process the queue using BFS. When we take a course, we add it to the result ordering and reduce the indegree of every course that depends on it.
6. If the indegree of a dependent course becomes `0`, it means all of its prerequisites have been completed, so we add that course to the queue.
7. We continue this process until the queue becomes empty. If the result contains all `numCourses` courses, the ordering is valid, so we return the result.
8. If the result contains fewer than `numCourses` courses, it means there is a cycle in the prerequisite graph. Since the courses involved in the cycle can never have an indegree of `0`, they cannot be added to the result, so we return an empty array.
9. The time complexity is `O(V + E)`, where `V` is the number of courses and `E` is the number of prerequisites, because every course and prerequisite relationship is processed at most once. The auxiliary space complexity is `O(V + E)` for the adjacency list, indegree array, queue, and result."""