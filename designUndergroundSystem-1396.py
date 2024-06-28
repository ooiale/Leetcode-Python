'''
  create two hashMaps, one to keep track of the people checked in,
  and another to keep track of the total time and number of people who
  have taken a route (start, end)
  all operations here are either updating, searching, deleting or creating new values in a hashMap so all methods are O(1) time
'''

class UndergroundSystem:

    def __init__(self):
        self.check = {} #id => [stationName, time]
        self.time = {} # (startStation, endStation) => avg time


    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.check[id]
        del self.check[id]
        key = (startStation, stationName)
        if key in self.time:
            self.time[key] = [self.time[key][0] + t - startTime, self.time[key][1] + 1]
        else:
            self.time[key] = [t - startTime, 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = (startStation, endStation)
        return self.time[key][0] / self.time[key][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)