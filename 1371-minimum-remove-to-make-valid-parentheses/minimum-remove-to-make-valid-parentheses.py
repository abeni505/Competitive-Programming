class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        stack = []
        output = []
        
        for i in s:
            if i == "(":
                stack.append(len(output))  
                output.append(i)

            elif i == ")":
                if stack:  
                    stack.pop()
                    output.append(i)
            else:
                output.append(i)
        
        for left in stack:
            output[left] = ''
            
        return ''.join(output)
