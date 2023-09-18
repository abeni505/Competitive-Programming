class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]

        for i in s:
            if stack and i =="*":
                stack.pop(-1)
            else:
                stack.append(i)

        return "".join(stack)
        