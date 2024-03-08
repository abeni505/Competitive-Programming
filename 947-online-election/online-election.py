class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times

    def calc(self,target):
        left = -1
        right = len(self.times)

        while left + 1 < right:
            mid = (left + right)//2

            if self.times[mid] > target:
                right = mid
            else:
                left = mid

        return left
  

    def q(self, t: int) -> int:
        
        indx = self.calc(t)

        count = Counter(self.persons[:indx + 1])

        max_ = max(count.values())

        
        allmax_ = [key for key , value in count.items() if value == max_]
        setmax = set(allmax_)

        if len(allmax_) > 1:
            while self.persons[indx] not in  setmax:
                indx -= 1
            return self.persons[indx]
            
        return allmax_[0]
        
        
        
    

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, self.)
# param_1 = obj.q(t)