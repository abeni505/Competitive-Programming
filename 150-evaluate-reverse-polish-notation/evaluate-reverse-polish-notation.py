class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        total = 0
        for i in tokens:
            if i == "+":
                if len(stack) >= 2:
                    total = stack.pop() + stack.pop()
                    stack.append(total)
            elif i == "-":
                if len(stack) >= 2:
                    a = stack.pop()
                    b = stack.pop()
                    total = b - a
                    stack.append(total)

            elif i == "*":
                if len(stack) >= 2:
                    total = stack.pop() * stack.pop()
                    stack.append(total)
            
            elif i == "/":
                if len(stack) >= 2:
                    a = stack.pop()
                    b = stack.pop()
                    total = int(b / a)
                    stack.append(total)
            else:
                total = int(i)
                stack.append(total)

        return total

                    
