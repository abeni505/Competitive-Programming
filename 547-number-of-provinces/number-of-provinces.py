class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        adjlist = defaultdict(set)

        for row in range(len(isConnected)):
            for col in range(len(isConnected[0])):
                if isConnected[row][col] == 1 and row != col:
                    adjlist[row].add(col)
                    adjlist[col].add(row)
        
        visited = set()
        count = 0
        for v in range(len(isConnected)):
            if v not in visited:
                count += 1
                stack = [v]
                visited.add(v)

                while stack:
                    curr = stack.pop()

                    for nbr in adjlist[curr]:
                        if nbr not in visited:
                            stack.append(nbr)
                            visited.add(nbr)
        return count

