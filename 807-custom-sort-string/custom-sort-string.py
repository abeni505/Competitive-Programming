class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
       
        count = Counter(s)
        output = []
       
        for i in order:
            if i in count:
    
                output.extend([i] * count[i])
                del count[i]

        for i in count:
            output.extend([i] * count[i])

       
        return "".join(output)