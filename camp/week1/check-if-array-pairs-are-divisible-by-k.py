class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        new = defaultdict(int)

        
        for i in arr:
            new[i % k] += 1

        for i in new:
            if i == 0:
                if new[i] % 2:
                    return False
            else:
                if new[-i % k] != new[i % k]:
                    return False
        
        return True