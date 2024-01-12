class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        left = count_v = 0
        vowels = {'a', 'e', 'i', 'o' , 'u'}
        window = s[:k]
        for i in window:
            if i in vowels:
                count_v += 1
        max_ = count_v

        for right in range(k , len(s)):
            if s[left] in vowels:
                count_v -= 1
            if s[right] in vowels:
                count_v += 1
                
            left += 1

            max_ = max(max_ , count_v)
            
        return max_