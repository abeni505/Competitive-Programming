class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()

        left = score = max_ = 0
        right = len(tokens) - 1

        while left <= right:
            if tokens[left] <= power:
                power -= tokens[left]
                score += 1
                left += 1
                max_ = max(max_,score)
            elif score > 0:
                score -= 1
                power += tokens[right]
                right -= 1
            
            else:
                break
        return max_
 
        