class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        def convert(word):
            digit = 0
            for i in word:
                digit = 10*digit + (ord(i)-ord("0"))
            return digit

        return str(convert(num1)*convert(num2))


                