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

#answer
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
    
#example usage
numCourses = 2
prerequisites = [[1,0]]
print(Solution().canFinish(numCourses, prerequisites))  # Output: true  
numCourses = 2
prerequisites = [[1,0],[0,1]]
print(Solution().canFinish(numCourses, prerequisites))  # Output: false

"""walkthrough
1. We first create an indegree list to keep track of the number of prerequisites for each course, and an adjacency list to represent the graph of courses and their dependencies.
2. We populate the indegree and adjacency list based on the prerequisites provided. 
3. We then initialize a queue with all courses that have an indegree of 0, meaning they have no prerequisites and can be taken immediately.
4. We perform a breadth-first search (BFS) by repeatedly taking courses from the queue, reducing the indegree of their dependent courses, and adding any courses that now have an indegree of 0 to the queue.
5. Finally, we check if the number of courses we were able to finish equals the total number of courses. If it does, we return true; otherwise, we return false, indicating that it's not possible to finish all courses due to a cycle in the prerequisites.       
"""