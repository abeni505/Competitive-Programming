class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        r = len(bank)
        c = len(bank[0])

        prev_row = 0
        total = 0

        for row in range(r):

            count_1 = 0
            for col in range(c):
                if bank[row][col] == "1":
                    count_1 += 1

            if count_1 != 0:

                total += count_1 * prev_row
                prev_row = count_1

        return total