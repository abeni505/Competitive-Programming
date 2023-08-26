class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        acr=""
        for i in words:
            acr+=i[0]
        return acr==s
        