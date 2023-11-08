class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []

        ans = ""

        for i in s :
            if i == "(" :
                if len(stack) >= 1:
                    ans+=i
                stack.append(i)
            elif i == ")":
                if len(stack) > 1:
                    ans += i
                stack.pop()
        return ans
