'''
  we want to create a hash map that stores a pair of values (val, time).
  the timestamp are given in increasing order therefore, we can use a 
  binary search to find the desired timestamp.
  since we are either looking for a time match or the most recent time that is 
  less than the timestamp given, everytime our middle pointer is <= timestamp, 
  we will consider that value, a potential one. because after that we update our 
  l pointer to l = m + 1 so we are discarting smaller times from the array
  time is O(1) for inserting
  time is O(logn) for searching
'''

class TimeMap:

    def __init__(self):
        self.map = {} #key => list(val, time)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.map.get(key, [])
        l = 0
        r = len(vals) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2
            if vals[m][1] <= timestamp:
                res = vals[m][0] #closest time < timestamp so far
                l = m + 1 #we update left to the right so currently, res
                #is the smallest time < timestamp in the next iteration 
            else:
                r = m - 1
        return res
