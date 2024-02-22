class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []
        path = path.split("/")
        print(path)

        for i in path:
            if i == "..":
                if stack:
                    stack.pop()
            elif i == "." or i == "":
                continue
            else:
                stack.append(i)

        output = ["/"]
        output.append("/".join(stack))

        return "".join(output)
