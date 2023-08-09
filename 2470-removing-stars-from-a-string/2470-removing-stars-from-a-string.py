class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        string = ""

        for i in range(len(s)):
            if s[i] == '*' and stack is not None:
                stack.pop()
            else:
                stack.append(s[i])
        for i in stack:
            string += i
        return string
    