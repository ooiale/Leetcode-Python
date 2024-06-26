'''
  students don't eat if at some point no students want to eat the sandwich on the top of the stack. so store a counter of the students and iterate through each sandwich until there are no students left who eat that sandwich
  time number of sandwiches left is the result
  time is O(n + m) where n is number of students m number of sandwiiches
  memory is O(1) since there are only 2 types of students
'''

from collections import defaultdict
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        #circle= 0
        #square = 1
        #sandwiches are on a stack, there is 1:1 ratio with students
        #if a student doesnt want the sandwich on top = goes to the end of line
        count = defaultdict(int) #count students 0s and 1s
        for i in students:
            count[i] += 1

        i = 0
        while i < len(sandwiches):
            sandwich = sandwiches[i]
            if count[sandwich] == 0:
                return len(sandwiches) - i
            count[sandwich] -= 1
            i += 1
        return 0