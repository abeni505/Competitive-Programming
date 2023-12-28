class Solution:
    def sortSentence(self, s: str) -> str:

        new_s = s.split()
        hashmap = dict()
        for i in new_s:
            hashmap[i[-1]] = i[:-1]

        sorted_hashmap = sorted(hashmap.items() , key = lambda x: x[0])

        output = []
        for key , value in sorted_hashmap:
            output.append(value)
        return " ".join(output)