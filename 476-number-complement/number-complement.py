class Solution:
    def findComplement(self, num: int) -> int:
       
        x = bin(num)
        new = []
        for i in range(2, len(x)):
            if x[i] == "1":
                new.append("0")
            else:
                new.append("1")
        
        b = "".join(new)
        
        return int(b, 2)

       