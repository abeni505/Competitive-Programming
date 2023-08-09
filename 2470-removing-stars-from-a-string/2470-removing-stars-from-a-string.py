class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        
        for i in s:
            if i=="*":
                stack and stack.pop()
            else:
                stack.append(i)


        return "".join(stack)
    