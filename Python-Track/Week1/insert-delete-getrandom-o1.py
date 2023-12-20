class RandomizedSet:

    def __init__(self):

        self.hashmap = dict()
        self.nums = []

    def insert(self, val: int) -> bool:
        if val not in self.hashmap:
            self.nums.append(val)
            self.hashmap[val] = len(self.nums) - 1
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.hashmap:
            temp = self.hashmap[val]
            self.hashmap[val] = len(self.nums)
            self.hashmap[self.nums[-1]] = temp
        

            self.nums[temp] , self.nums[-1] = self.nums[-1] , self.nums[temp]
            self.nums.pop()
            self.hashmap.pop(val)
            
            return True
        return False


    def getRandom(self) -> int:
        
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()