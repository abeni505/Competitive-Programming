class Solution:
    def maxLength(self, arr: List[str]) -> int:

        charSet = set()
        
        def overlap(s, charSet):
            c = Counter(s) + Counter(charSet)
            return any( val > 1 for val in c.values()) 


        def backtrack(idx):
            if idx == len(arr):
                return len(charSet)
            
            take = 0
            if not overlap(arr[idx], charSet):
                for ch in arr[idx]:
                    charSet.add(ch)
                take = backtrack(idx+1)
                for ch in arr[idx]:
                    if ch in charSet:
                        charSet.remove(ch)

            notTake = backtrack(idx+1)
            
            return max(take,notTake)
        
        return backtrack(0)