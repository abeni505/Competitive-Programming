class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:

        freq = [0] * n

        for road in roads:
            freq[road[0]] += 1
            freq[road[1]] += 1

        freq.sort()

        ans = 0
        for i in range(n):
            ans += (i + 1) * freq[i]

        return ans