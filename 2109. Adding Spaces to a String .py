class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        char=0
        for i in spaces:
            s=s[:i+char]+" "+s[i+char:]
            char+=1
        return s
