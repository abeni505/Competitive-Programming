class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        memo = {}

        def dp(i, jump):
            if i == stones[-1]:
                return True

            if (i, jump) not in memo:
                for new in [jump - 1, jump, jump + 1]:
                    if new > 0:
                        pos = i + new
                        if pos in stones:
                            if dp(pos, new):
                                memo[(i, jump)] = True
                                return True

            memo[(i, jump)] = False
            return False

        return dp(stones[0], 0)

