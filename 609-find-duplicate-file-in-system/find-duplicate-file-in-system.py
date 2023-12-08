class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:

        hashmap = defaultdict(list)

        for i in paths:

            path = i.split()
            
            for j in range(1,len(path)):
                
                txt , name = path[j].split("(")
                name = name[:-1]
                hashmap[name].append(path[0] + "/" + txt)
        

        out_put = []
        for k in hashmap:
            if len(hashmap[k]) > 1:
                out_put.append(hashmap[k])

        return out_put















        #     path = i.split()
        #     for j in range(1,len(path)):
        #         a,b = path[j].split("(")
        #         b=b[:-1]
        #         hashmap[b].append(path[0]+"/"+a)
        # return [hashmap[i] for i in hashmap if len(hashmap[i]) > 1 ]

