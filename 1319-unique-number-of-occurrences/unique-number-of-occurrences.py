class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        count_val = Counter(count.values())

        return len(set(arr)) == len(count_val.keys())