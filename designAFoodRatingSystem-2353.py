'''
  we will keep a hashMap that we can search the cuisine and the rating given a food
  the issue lies on our second map where we need to get the highest rated food based
  on cuisine. to do this we would need a hashMap that given the cuisine, returns
  a sorted list by rating of the foods. one idea would be a maxHeap but then removal
  would be O(n) instead of O(logn). 
  this SortedSet used a balanced BST to sort its elements
  building this sortedSet is O(n log n)
  changeRating is O(log n) from removal/ adding a new element
  highestRating is O(1)
'''

from collections import defaultdict
from typing import List
from sortedcontainers import SortedSet

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foodMap = {} #food => [cuisine, rating]
        self.cuisineMap = defaultdict(SortedSet) #cuisine => (rating, food) ordered by rating

        for i in range(len(foods)):
            self.cuisineMap[cuisines[i]].add((-ratings[i], foods[i]))
            self.foodMap[foods[i]] = [cuisines[i], ratings[i]]

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, rating = self.foodMap[food]
        self.foodMap[food][1] = newRating
        self.cuisineMap[cuisine].remove((-rating, food))
        self.cuisineMap[cuisine].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.cuisineMap[cuisine][0][1] #0th indexed = high rating, 


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
