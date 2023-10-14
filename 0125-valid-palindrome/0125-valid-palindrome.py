class Solution:
    def isPalindrome(self, s: str) -> bool:
        news=""
        for i in s:
            if i.isalnum():
                news+=i.lower()

        left=0
        right=len(news)-1

        while left<right :
            if news[left]!=news[right]:
                return False
            left+=1
            right-=1
        return True

        