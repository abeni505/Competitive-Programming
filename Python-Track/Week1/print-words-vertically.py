class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        
        max_ = 0
        for char in s:
            max_ = max(max_,len(char))
        out_put = [""]*max_

        for index in range(len(s)):
            if len(s[index]) < max_:
                s[index] += " "*(max_ - len(s[index]))
        print(s)
        for i in range(len(s)):
            for j in range(len(s[i])):
                out_put[j] += s[i][j]
        print(out_put)

        for word_i in range(len(out_put)):
            out_put[word_i] = out_put[word_i].rstrip()
    
        return out_put

        