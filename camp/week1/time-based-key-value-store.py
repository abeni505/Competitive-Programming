class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        self.hashmap[key].append((value,timestamp))
        
    def checker(self,value , time):
        left = 0
        right = len(value)

        while left + 1 < right:
            mid = (left + right) //2
            if value[mid][1] <= time:
                left = mid
            else:
                right = mid

        if not value  or value[left][1] > time:
            return ""
        else:
            return value[left][0]  




    def get(self, key: str, timestamp: int) -> str:
        
        return self.checker(self.hashmap[key] , timestamp )
         
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)