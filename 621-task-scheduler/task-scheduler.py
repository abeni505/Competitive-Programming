class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        freq = list(Counter(tasks).values())
        max_ = max(freq)
        max_Count = freq.count(max_)
            
        ans = (max_ - 1) * (n + 1) + max_Count
        

        return max(ans, len(tasks))