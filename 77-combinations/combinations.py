class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        output = []
        
        def backtrack(num , path):
            if len(path) == k:

                output.append( path[:])
                return
            
            for num in range(num , n + 1):
                path.append(num)
                backtrack(num + 1 , path)
                path.pop()

        backtrack(1 , [])
        return output
