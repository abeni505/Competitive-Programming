class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        
        out_put = []
        
        for i in range(len(variables)):
            
            if ((variables[i][0] ** variables[i][1] % 10) ** variables[i][2]) % variables[i][3] == target:
                out_put.append(i)
                    
                     
        return out_put
                    
        