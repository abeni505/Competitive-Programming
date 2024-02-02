class Solution:
    def sequentialDigits(self, low, high):
        
        digit = "123456789"
        output = []

        for i in range(len(digit)):
            for j in range(i + 1, len(digit)):
                check = int(digit[i:j + 1])

                if low <= check <= high:
                    output.append(check)

        output.sort()
        return output
