class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:

        right = 0
        new_str = ""
        for left in range(len(s)):
            if right < len(spaces) and left == spaces[right]:
                new_str += " "
                new_str += s[left]
                right+=1
            else:
                new_str+=s[left]

        return new_str