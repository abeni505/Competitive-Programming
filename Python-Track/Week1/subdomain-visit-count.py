class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        count_visit = defaultdict(int)
        for i in cpdomains:
            val , key = i.split()

            keys = key.split(".")
            for j in range(0,len(keys)):
                valid = ".".join(keys[j:])

                count_visit[valid] += int(val)

        out_put = []
        for key , value in count_visit.items():
            out_put.append(str(value) + " " + key)
            
        return out_put