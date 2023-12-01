class Solution:
    def romanToInt(self, s: str) -> int:
        
        dict1 = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        dict2 = {"I":1,"V":2,"X":3,"L":4,"C":5,"D":6,"M":7}

        window = {"I","X","C"}
        total_sum = 0
        i = 0

        while i < len(s):
            if s[i] not in window:
                total_sum += dict1[s[i]]

            else:
                if i+1 < len(s) and dict2[s[i]] < dict2[s[i+1]]:
                    total_sum += dict1[s[i+1]]- dict1[s[i]]
                    i += 1
                else:
                    total_sum += dict1[s[i]]
            i += 1

        return total_sum


