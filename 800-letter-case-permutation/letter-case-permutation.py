class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        output = []
        def backtrack(i , sub):
            if len(sub) == len(s):
                output.append(sub)
            else:
                if s[i].isalpha():
                    backtrack(i + 1 , sub + s[i].swapcase())

                backtrack(i + 1, sub + s[i])
        
        backtrack(0 , "")
        return output