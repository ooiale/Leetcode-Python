'''
  move along the cartesian plane and add to the visited set the coordinates
  you have already been. once you are in a coordinate in visited, it means
  the paths have crossed
  time is O(n)
'''

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        up = 0
        side = 0
        i = 0
        visited = set() #(up, side) => visited
        while i < len(path):
            visited.add((up, side))
            if path[i] == "N":
                up += 1
            elif path[i] == "S":
                up -= 1
            elif path[i] == "E":
                side += 1
            elif path[i] == "W":
                side -= 1
            if (up, side) in visited:
                return True
            i += 1
        return False