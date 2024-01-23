class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        

        visited = set()
        output = set()

        for i in range(len(s)-9):
            window = s[i:i+10]

            if window in visited:
                output.add(window)
            else:
                visited.add(window)

        return list(output)
