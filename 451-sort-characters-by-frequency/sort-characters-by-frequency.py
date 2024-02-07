class Solution:
    def frequencySort(self, s: str) -> str:
        
        count = Counter(s)

        keys = [i for i in count.keys()]
        
        keys = sorted(keys, key = lambda x : count[x] , reverse = True)

        output = []
        for i in range(len(keys)):
            for k in range(count[keys[i]]):
                output.append(keys[i])

        return "".join(output)