'''
  lets think of this problem as a graph where a course i with requirements j represents the node i with an edge (i ,j) pointing to the node j.
  in this case, we can run a DFS through every node and visit its edges. if at some point we find a loop (which we can track using a set to track the current path on the current DFS) we return false.
  lets store the info about the nodes and its edges in a hashMap, where hashMap[i] =[j, k, ...] => adjacency list: good when number of edges is smaller than the maximum number of edges possible
  the base case for this recursive DFS will be either a node with no edges or a node that was 
  already visited (loop).
  for efficiency purposes, when we determine a class can be completed, we change its edges to empty
  so that it technically becomes a base case for future visits.
  Time is O(nodes + edges) = O(numCourses + len(prerequisites))
'''

from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {i: [] for i in range(numCourses)}
        for c, p in prerequisites:        
            courses[c].append(p)

        visited = set()

        def dfs(course):
            #base cases
            if course in visited:
                return False
            if courses[course] == []:
                return True
            
            #confirm visit
            visited.add(course)
            #continue the dfs on neighbors
            for neighbors in courses[course]:
                #loop found return false immediatelly
                if not dfs(neighbors):
                    return False
            #dfs went smoothly and is now backtracking
            visited.remove(course)
            courses[course] = []
            return True

        #perform DFS on all nodes in case the graph is not connected.
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
            