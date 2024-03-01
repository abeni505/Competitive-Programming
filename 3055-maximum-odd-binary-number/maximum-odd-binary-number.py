class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        
        count = Counter(s)
        one = count["1"]
        zero = count["0"]

        output = []
        for i in range(one -1):
            output.append("1")
        for j in range(zero):
            output.append("0")

        output.append("1")


        return "".join(output)