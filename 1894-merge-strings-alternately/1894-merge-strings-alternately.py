class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left,right=0,0
        news=""
        while left<len(word1) and right<len(word2):
            news+=word1[left]
            news+=word2[right]
            left+=1
            right+=1
        news+=word1[left:]
        news+=word2[right:]
        

        return news

        