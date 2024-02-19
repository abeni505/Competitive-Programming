class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        count = Counter()

        for i in bills:
            if i == 5:
                count[5] += 1
            elif i == 10:
                count[i] += 1
                if count[5]:
                    count[5] -= 1
                else:
                    return False
            else:
                count[i] += 1
                if count[5] and count[10]:
                    count[5] -=1
                    count[10] -= 1
                elif count[5] >= 3:
                    count[5] -= 3
                else:
                    return False
    
        return True
