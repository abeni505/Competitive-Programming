class Solution:
    def largestOddNumber(self, num: str) -> str:


        new_str = ""
        for i in range(len(num)-1,-1,-1):
            if int(num[i]) % 2 != 0 :
                new_str = num[:i+1]
                break

        return new_str
                
