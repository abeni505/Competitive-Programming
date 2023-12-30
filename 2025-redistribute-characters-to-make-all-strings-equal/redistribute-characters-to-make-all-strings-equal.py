class Solution:
    def makeEqual(self, words: List[str]) -> bool:


        hashmap = defaultdict(int)

        for i in words:
            for j in i:
                hashmap[j] += 1

        for val in hashmap.values():
            if val % len(words) != 0:
                return False

        return True
        