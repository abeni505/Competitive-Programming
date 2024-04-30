class Solution:
    def wonderfulSubstrings(self, word: str) -> int:

        bitmask = 0
        counter = defaultdict(int)
        counter[0] = 1
        res = 0

        for ch in word:
            chInd = ord(ch) - ord('a')
            bitmask ^= (1 << chInd)
            res += counter[bitmask]


            for i in range(10):
                b = bitmask ^ (1 << i)
                res += counter[b]

            counter[bitmask] += 1

        return res