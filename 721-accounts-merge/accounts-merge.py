class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        root = [i for i in range(n)]
        rank = [0] * n

        def find(x):
            while x != root[x]:
                x = root[x]
            return x

        def union(x , y):
            root_x = find(x)
            root_y = find(y)

            if root_x != root_y:
                if rank[root_x] > rank[root_y]:
                    root[root_y] = root_x
                elif rank[root_x] < rank[root_y]:
                    root[root_x] = root_y
                else:
                    root[root_x] = root_y 
                    rank[root_y] += 1

        visited = defaultdict(int)
        for i in range(n):
            for j in range(1 , len(accounts[i])):
                email = accounts[i][j]
                if email in visited:
                    union(i , visited[email])
                
                else:
                    visited[email] = i
        
        temp = defaultdict(set)
        for i in range(len(accounts)):
            common = find(i)
            for email in accounts[i][1:]:
                temp[common].add(email)

        ans = []
        for key , val in temp.items():
            name = accounts[key][0]
            email = sorted(val)

            ans.append([name] + email)
    
        return ans
