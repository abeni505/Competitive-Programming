class Solution:
    def interpret(self, command: str) -> str:
        new = ""
        i = 0
        while i < len(command):
            if command[i] == '(' and command[i + 1] == ')':
                new += 'o'
                i += 2
            elif command[i] == '(' or command[i] == ')':
                i += 1
            else:
                new += command[i]
                i += 1
        return new
