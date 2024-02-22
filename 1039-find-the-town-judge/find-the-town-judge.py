class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        hashmap = Counter()
        hasha = Counter()

        if n == 1 and len(trust) == 0:
            return 1
        for a , b in trust:
            hashmap[b] += 1
            hasha[a] += 1
        
        for key , val in hashmap.items():
            if val == n - 1  and key not in hasha.keys():
                return key
        
        return -1
        
        