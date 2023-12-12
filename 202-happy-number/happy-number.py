class Solution:
    def isHappy(self, n: int) -> bool:
        

        hashset = set()

        str_n = str(n)
        def operation (str_n):
            int_n = 0
            for i in range(len(str_n)):
                int_n += int(str_n[i]) ** 2

            return int_n

    
        while int(str_n) > 1:      
            str_n = str(operation(str_n))
            if str_n in hashset:
                break
            hashset.add(str_n)

        return int(str_n) == 1


