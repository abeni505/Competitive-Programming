class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        max_ = max(to_ for numPass , from_ , to_ in trips)

        prefix = [0] * (max_ + 1)

        for numPass , from_ , to_ in trips:
            prefix[from_] += numPass
            prefix[to_] -= numPass

        pre_sum = 0
        for i in range(len(prefix)):
            prefix[i] = pre_sum + prefix[i]
            pre_sum = prefix[i]
            
            if pre_sum > capacity:
                return False
        
        return True
        
