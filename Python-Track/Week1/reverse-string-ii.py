class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        i = 0
        new_s = []
        while i < len(s) :
            rev = s[i:i+k]
            new_s.append(rev[::-1])
            new_s.append(s[i+k : min(len(s)+1 ,2*k + i )])
            i += 2*k

        return "".join(new_s)