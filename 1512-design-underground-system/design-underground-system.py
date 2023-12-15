class UndergroundSystem:

    def __init__(self):
        self.trips = {}
        self.two_places = defaultdict(list)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        trip = [stationName, t]
        self.trips[id] = trip
        
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        diff = t - self.trips[id][1]

        start_station = self.trips[id][0] 
        end_station = stationName

        self.two_places[(start_station , end_station)].append(diff)
       
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        if (startStation , endStation) in self.two_places :
            return sum(self.two_places[(startStation , endStation)])/len(self.two_places[(startStation , endStation)])
        else:
            return 0

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)