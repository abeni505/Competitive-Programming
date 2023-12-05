class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"

        out_put = []
        for i in words:
            
            if all(char in row1 for char in i.lower()) or all(char in row2 for char in i.lower()) or all(char in row3 for char in i.lower()):
                out_put.append(i)
        
        return out_put
