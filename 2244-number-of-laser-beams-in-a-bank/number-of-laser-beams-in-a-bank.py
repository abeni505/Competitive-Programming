class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        r = len(bank)
        c = len(bank[0])

        prev_row = 0
        total = 0

        for row in bank:

            count_1 = row.count("1")

            if count_1 != 0:

                total += count_1 * prev_row
                prev_row = count_1

        return total