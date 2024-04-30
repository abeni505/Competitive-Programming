class Solution:
    def countBits(self, n: int) -> List[int]:
        
        Total = []

        def count_1(n):
            
            count_1 = 0
            while n != 0:
                q = n // 2
                r = n % 2

                if r == 1:
                    count_1 += 1
                n = q
            
            return count_1
        
        output = []
        for i in range(n + 1):
            output.append(count_1(i))
        
        return output