class Solution:
    def isValid(self, word: str) -> bool:
        
        if len(word) < 3:
            return False
        
        vowel = {'a','e','i','o','u','A','E','I','O','U'}

        hasvowel = False
        hasconso = False

        for chr in word:

            if chr in vowel:
                hasvowel = True
            elif chr.isalpha():
                hasconso = True
            elif chr.isdigit():
                continue
            else:
                return False

            
        return hasvowel and hasconso 
