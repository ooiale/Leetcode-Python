'''
  initialize the class with a hashMap that will keep track of the
  points added (x, y) and the quantity of these points.
  To see if we can make squares given a point (px, py), we will first find
  all points that form a perfect diagonal with (px, py). once we have 
  found the diagonal we know the remanining points are (x, py), (px, y).
  because we can have multiple of these 3 points, for every square we make,
  we increment the result by the product of the quantity of those points
  time is O(n) since we iterate through all points once to find the diagonals
  and because search in a hashMap is O(1), finding the other 2 points are O(1)
'''

from typing import List


class DetectSquares:

    def __init__(self):
        self.points = {} #(x, y) => amount

    def add(self, point: List[int]) -> None:
        self.points[(point[0], point[1])] = 1 + self.points.get((point[0], point[1]), 0)

    def count(self, point: List[int]) -> int:
        #step 1 find points in the same diagonal
        res = 0
        px, py = point
        for x, y in self.points.keys():
            if x == px or y == py or abs(py - y) != abs(px - x):
                continue
            if (x, py) in self.points and (px, y) in self.points:
                res += self.points[(x, py)] * self.points[(px, y)] * self.points[(x, y)]
        return res
        #step 2 find if x, py and px, y exist


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)