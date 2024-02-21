class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        
        hashmap = set()
        total = 0

        count = Counter(answers)
        # for i in answers:
        #     if i not in hashmap or i == 0:
        #         hashmap.add(i)
        #         total += (i + 1)
        # #    
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