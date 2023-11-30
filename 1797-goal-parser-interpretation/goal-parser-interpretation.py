class Solution:
    def interpret(self, command: str) -> str:

        new_str = ""

        for i in range(len(command)):
            if command[i] == "G":
                new_str += "G"
            elif command[i] == "(":
                if command[i+1] == ")":
                    new_str += "o"
                else:
                    new_str += "al"
        return new_str
