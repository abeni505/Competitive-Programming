class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        left=0
        s=sorted(s)
        t=sorted(t)
        return (s==t)
