class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        path = []
        output = []

        def backtrack(indx):

            if len(path) == k:
                output.append(path[:])
                return
            
            for i in range(indx , n + 1):
                path.append(i)
                backtrack(i + 1)
                path.pop()

        backtrack(1)
        return output