class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:

        
        left = 0
        right = 0
        new_str = []
        while right < len(s) and left < len(spaces):

            if right < spaces[left]:
                new_str.append(s[right])
            elif right == spaces[left]:
                new_str.append(" ")
                new_str.append(s[right])
                left += 1

            right += 1

        new_str.append(s[right:])

        return "".join(new_str)