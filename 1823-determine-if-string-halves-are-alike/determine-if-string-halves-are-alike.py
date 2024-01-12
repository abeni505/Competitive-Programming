class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        hashset = {'a' , 'e' , 'i' , 'o' , 'u' , 'A' , 'E' , 'I' , 'O' , 'U'}

        total = left_count = 0
        for i in s:
            if i in hashset:
                total += 1
                
        for j in range(len(s)//2):
            if s[j] in hashset:
                left_count += 1
        
        return total - left_count == left_count
 