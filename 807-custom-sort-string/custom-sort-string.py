class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
       
        count = Counter(s)
        output = []
        new = []
        
        for i in order:
            if i in count:
                for _ in range(count[i]):
                    output.append(i)
                del count[i]

        for i in count:
            for _ in range(count[i]):
                new.append(i)
        
        new.sort()
        output.extend(new)
       
        return "".join(output)