class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        

        root = defaultdict(str)
        for i in range(26):
            root[chr(ord("a") + i)] = chr(ord("a") + i)
        
        def find(x):
            while x != root[x]:
                x = root[x]

            return x

        def union(x , y):
            rootx = find(x)
            rooty = find(y)

            root[rootx] = root[rooty] = min(rootx, rooty)
    
                   
        for i in range(len(s1)):
            union(s1[i], s2[i])
     
        
        output = []
        for j in baseStr:
            output.append(find(j))

        return "".join(output)





        return ""