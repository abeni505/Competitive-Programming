class Solution:
    def maximum69Number (self, num: int) -> int:
        
        n = list(str(num))
        
        for i in range(len(n)):
            if n[i] != "9":
                n[i] = "9"
                break
        return int("".join(n))
