'''
  we will use djisktra algorithm here. thats an algorithm to find minimum cost path in a graph.
  basically we will do a BFS search using a minHeap instead of a queue.
  so we start by creating the adjacency list with all edges.
  then, starting from the given node with cost 0 we start the algorithm.
  we will perform BFS by taking the node with min cost from the heap (as opposed to the FIFO from a queue). then we append to the heap all adjacent nodes with a new cost of curNode.cost + adjNode.cost. We keep a track of visited nodes because if are visiting nodes by minimum cost so in a loop, the second time visiting a node will always be a worse cost.
  time is O(Elog(E)). the log(E) comes from the operations in the heap. and E is the number of edges.
'''


from collections import defaultdict
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        heap = []
        for n1, n2, w in times:
            adj[n1].append([n2, w])
        
        visited = set()
        heap = [[0, k]] #[weight, node] because heapq sorts by first value of the list by default
        res = -1
        while heap:
            weight, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            res = max(res, weight)
            for nei, w in adj[node]:
                if nei not in visited:
                    heapq.heappush(heap, [weight + w, nei])

        return res if len(visited) == n else -1