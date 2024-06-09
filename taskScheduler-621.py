'''
  we always want to complete the task that has the most amount left to do
  so in order to always have access to the biggest value, we will use a 
  max heap.
  every time we complete a task, the amount of this task is increased by 1
  and we will add this amount to a queue, paired with the time this task
  will be refreshed. 
  everytime the oldest element from the queue gets refreshed, we add it back
  to the heap.
  time is O(n) for iterating through each task once, since operations
  with the Heap is O(log26) we have at most 26 values in it
'''

from collections import Counter, deque
import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        queue = deque([]) #pair [- count, refresh time]
        taskCount = Counter(tasks)
        maxHeap = [-i for i in taskCount.values()]
        heapq.heapify(maxHeap)
        time = 0
        while maxHeap or queue:
            time += 1
            if maxHeap:
                val = heapq.heappop(maxHeap) #its the negative count here
                val += 1
                if val != 0:
                    queue.append((val, time + n))
            if queue and queue[0][1] <= time:
                task = queue.popleft()
                heapq.heappush(maxHeap, task[0])
        return time
