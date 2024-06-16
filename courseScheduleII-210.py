'''
  so we will treat this as a graph problem. So first we create
  an adjacency list so we can run dfs on all nodes.
  if we ever bump into a cycle, we know the problem is impossible.
  the difference from courseSchedule1 is that now we will need to
  not visit courses we have already visited and this could be done
  just with the completed course list but search in it is O(n) so
  instead we use this doneSet = set() to keep track of those just because
  search is O(1) in it.
  time is O(v + e)
'''

from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = {i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            courses[c].append(p)

        visited = set()
        doneSet = set()
        done = []

        def dfs(course):
            if course in visited:
                return False
            if course in doneSet:
                return True

            visited.add(course)

            for pre in courses[course]:
                if not dfs(pre):
                    return False
            
            visited.remove(course)
            doneSet.add(course)
            done.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return done
            