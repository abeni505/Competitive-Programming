class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n=len(citations)
        citations.sort()
        max_index=0
        for i in range(n):

            max_index=max(max_index,min(citations[i],n-i))

        return max_index
       