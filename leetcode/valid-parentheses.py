class Solution:
    def isValid(self, s: str) -> bool:
        
       
        stack = []
        check = {")":"(" , "]":"[" ,"}":"{"}

        for i in s:
            if i in check.values():
                stack.append(i)
            else:
                if stack and stack[-1] == check[i]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0