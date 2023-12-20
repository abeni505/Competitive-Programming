class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        str_digit = "".join(map(str,digits))

        int_ = int(str_digit) + 1

        return [int(char) for char in str(int_)]