class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        out_put = [0]*len(s)
        for i in range(len(indices)):
            out_put[indices[i]] = s[i]

        return "".join(out_put)
