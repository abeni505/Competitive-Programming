class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def helper(target):
            curr = count = 0

            for i in piles:
                count += ceil(i/target)

            return count
        
        left = 0
        right = max(piles) + 1

        while left + 1 < right:
            mid = (left + right)//2

            if helper(mid) <= h:
                right = mid
            else:
                left = mid
        
        return right


        


