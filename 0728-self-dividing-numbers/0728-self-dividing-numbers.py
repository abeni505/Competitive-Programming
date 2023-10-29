class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        arr = []
        for i in range(left, right + 1):
            str_digit = str(i)
            is_self_dividing = True

            for j in str_digit:
                if int(j) == 0 or i % int(j) != 0:
                    is_self_dividing = False
                    break

            if is_self_dividing:
                arr.append(i)

        return arr