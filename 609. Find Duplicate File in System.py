class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hashmap=defaultdict(list)

        for i in paths:
            path = i.split()
            for j in range(1,len(path)):

                a,b=path[j].split('(')
                b = b[:-1]
                hashmap[b].append(path[0]+'/'+a)

        return [hashmap[k] for k in hashmap if len(hashmap[k]) > 1]

       
