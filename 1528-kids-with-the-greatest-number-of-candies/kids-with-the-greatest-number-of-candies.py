class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        out_put = []
        max_ = max(candies)
        for i in candies:
            if i + extraCandies >= max_:
                out_put.append(True)
            else:
                out_put.append(False)
        return out_put
