class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        pre_sum = [0] * (len(s) + 1)

        for x, y, z in shifts:
            if z == 0:
                pre_sum[x] -= 1
                pre_sum[y + 1] += 1
            else:
                pre_sum[x] += z
                pre_sum[y + 1] -= z

        run_sum = 0
        for i in range(len(pre_sum)):
            pre_sum[i] = run_sum + pre_sum[i]
            run_sum = pre_sum[i]

        new_s = [ord(i) for i in s]

        output = [chr((pre_sum[j] + new_s[j] - ord("a")) % 26 + ord("a")) for j in range(len(s))]

        return "".join(output)

