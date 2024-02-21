class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        

        total = 0
        count = Counter(answers)
        for key , value in count.items():
            if key == 0:
                total += value
            else:
                if key > value:
                    total += key + 1
                else:
        
                    q= (value //(key + 1))
                    r = value % (key + 1)
                    total += q * (key + 1)
                    total += key + 1 if r else 0
    
        return total 