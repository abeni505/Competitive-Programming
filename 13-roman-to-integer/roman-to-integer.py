class Solution:
    def romanToInt(self, s: str) -> int:
        dict_ = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

        total_sum = 0
        i = 0
        while i < len(s)-1:
            if s[i] == "I" and s[i+1] == "V":
                total_sum += 4
                i+=1

            elif s[i] == "I" and s[i+1] == "X":
                total_sum += 9
                i+=1

            elif s[i] == "X" and s[i+1] == "L":
                total_sum += 40
                i+=1

            elif s[i] == "X" and s[i+1] == "C":
                total_sum += 90
                i+=1

            elif s[i] == "C" and s[i+1] == "D":
                total_sum += 400
                i+=1
            elif s[i] == "C" and s[i+1] == "M":
                total_sum += 900
                i+=1
            elif s[i] == "I" and s[i+1] == "I":
                total_sum +=  len(s[i:])
                i = len(s)
                break
                
            else:
                # if not s[i+1]:
                #     total_sum += dict_[s[i]]
                #     total_sum += dict_[s[i+1]]
                # else:
                #     total_sum += s[i]
                total_sum += dict_[s[i]]
                    
            i += 1
            print(total_sum)
        if i < len(s):
            total_sum += dict_[s[i]]
        
        
        return total_sum
          