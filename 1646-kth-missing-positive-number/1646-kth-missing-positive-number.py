class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
    
        missing=[]
        for i in range(1,10000):
            if i not in arr:
                missing.append(i)
        
        if k-1>len(missing):
            return max(missing)

        return missing[k-1]
