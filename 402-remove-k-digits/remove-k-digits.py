class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        stack = []

        for digit in num:
            while stack and k and stack[-1] > digit:
                stack.pop()
                k -= 1
            
            if stack or digit != "0":
                stack.append(digit)
            
        if k: 
            stack = stack[0: -k]
                
        return ''.join(stack) or '0'

            

