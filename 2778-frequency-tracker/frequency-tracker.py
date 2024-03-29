class FrequencyTracker:

    def __init__(self):
        self.freq = defaultdict(int)
        self.count = defaultdict(int)
        

    def add(self, number: int) -> None:
        self.freq[number] += 1
        self.count[self.freq[number]] += 1
        self.count[self.freq[number] - 1] -= 1
        

    def deleteOne(self, number: int) -> None:
        if self.freq[number]:
            self.count[self.freq[number]] -= 1
            self.freq[number] -= 1
            self.count[self.freq[number]] += 1
        

    def hasFrequency(self, frequency: int) -> bool:
        
        return self.count[frequency] > 0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)