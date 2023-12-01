class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left = 0
        right = 0
        new_str = ""

        while left<len(word1) and right < len(word2):
            new_str += word1[left]
            new_str += word2[right]
            
            left += 1
            right += 1
        if left == len(word1):
            new_str += word2[right:]
        if right == len(word2):
            new_str += word1[left:]


        return new_str
