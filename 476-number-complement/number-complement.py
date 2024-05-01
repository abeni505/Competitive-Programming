class Solution:
    def findComplement(self, num: int) -> int:
       
        ones_comp = ~num 
        y =  2 ** (num.bit_length())

        return ones_comp + y

       