class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
       
        ziped = set(zip(s , t))

        return len(ziped) == len(set(s)) == len(set(t))


