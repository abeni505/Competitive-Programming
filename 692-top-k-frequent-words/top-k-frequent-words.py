class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        count = Counter(sorted(words))

        max_heap = [(-val , key) for key , val in count.items()]
        heapify(max_heap)

        output = []
        for _ in range(k):
            output.append(heappop(max_heap)[1])

        return output

        
