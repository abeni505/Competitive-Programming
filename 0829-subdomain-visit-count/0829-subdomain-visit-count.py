class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hashmap = {}
        for i in cpdomains:
            a = i.split(" ")
            b = a[1].split(".")
            for i in range(0, len(b)):
                c = ".".join(b[i:])
                if c in hashmap:
                    hashmap[c] = int(hashmap[c]) + int(a[0])
                else:
                    hashmap[c] = int(a[0])

        arr = []
        for i in hashmap:
            arr.append(str(hashmap[i]) + " " + i)

        return arr
