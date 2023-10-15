def convertToInteger(s):
    num = 0
    n = len(s)
    for i in s:
        num = num * 10 + (ord(i) - 48)
    return(num)

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1,num2 = convertToInteger(num1),convertToInteger(num2)
        return (str(num1*num2))

        
        