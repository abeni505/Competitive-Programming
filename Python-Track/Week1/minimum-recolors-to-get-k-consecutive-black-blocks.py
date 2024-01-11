class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        window = blocks[:k]
        
        count = Counter(window)


        min_ = count["W"]

        for i in range(k,len(blocks)):
            count[blocks[i]] += 1 
            count[blocks[i - k]] -= 1 
            min_ = min(min_, count["W"])

        return min_
