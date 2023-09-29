class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in s:
            if i != "]":
                stack.append(i)
            else:
                sub_string = ""
                while stack[-1] != "[":
                    sub_string = stack.pop() + sub_string
                stack.pop()

                repetition_count = ""
                while stack and stack[-1].isdigit():
                    repetition_count = stack.pop() + repetition_count

                stack.append(int(repetition_count) * sub_string)

        return "".join(stack)
