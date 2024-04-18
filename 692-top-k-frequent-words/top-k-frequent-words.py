class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        count = Counter(sorted(words))

        output = [key for key , val in count.most_common(k)]
        return output
