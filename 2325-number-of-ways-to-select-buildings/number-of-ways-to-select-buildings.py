class Solution:
    def numberOfWays(self, s: str) -> int:
        
        zero = s.count('0')
        one = s.count('1')

        prev_one = prev_zero = total = 0
        for i in s:
            if i == '1':
                total += prev_zero * (zero - prev_zero)
                prev_one += 1
            else:
                total += prev_one * (one - prev_one)
                prev_zero += 1
        
        return total

