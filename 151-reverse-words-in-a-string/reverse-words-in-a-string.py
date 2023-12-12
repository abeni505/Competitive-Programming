class Solution:
    def reverseWords(self, s: str) -> str:

        s = s.strip()
        out_put = s.split()

        return " ".join(reversed(out_put))