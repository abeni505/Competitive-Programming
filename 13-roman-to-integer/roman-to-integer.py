class Solution:
    def romanToInt(self, s: str) -> int:
        
        dict1 = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        
        s = s.replace("IV","IIII")
        s = s.replace("IX","VIIII")
        s = s.replace("XL","XXXX")
        s = s.replace("XC","LXXXX")
        s = s.replace("CD","CCCC")
        s = s.replace("CM","DCCCC")

        total_sum = 0
    
        for i in s:
            total_sum += dict1[i]

        return total_sum

        


