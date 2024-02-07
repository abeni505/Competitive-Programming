class Solution:
    def frequencySort(self, s: str) -> str:
        
        count = Counter(s)

        keys = [i for i in count.keys()]
        
        keys = sorted(keys, key = lambda x : count[x])
        keys = keys[::-1]

        output = []
        for i in range(len(keys)):
            for k in range(count[keys[i]]):
                output.append(keys[i])

        return "".join(output)