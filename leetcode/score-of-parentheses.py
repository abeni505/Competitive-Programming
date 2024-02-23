class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        stack = []

        total = 0
        for i in s:
            if i == ")":
                if stack:
                    total = stack.pop() + max(1, total * 2)
        
            else:
                stack.append(total)
                total = 0
                
        return total 


