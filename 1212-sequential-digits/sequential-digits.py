class Solution:
    def sequentialDigits(self, low, high):
        c = "123456789"
        output = []

        for i in range(len(c)):
            for j in range(i + 1, len(c) + 1):
                cheeck = int(c[i:j])
                if low <= cheeck <= high:
                    output.append(cheeck)

        output.sort()
        return output

