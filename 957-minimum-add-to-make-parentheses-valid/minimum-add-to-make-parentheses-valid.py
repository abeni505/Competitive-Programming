class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        stack = []
        count = 0
        for i in s:
            if i == ")":
                if stack:
                    stack.pop()
                else:
                    count += 1
            else:
                stack.append(i)
       
        return count + len(stack)
        