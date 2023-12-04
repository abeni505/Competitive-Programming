class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:

        new_1 = ""
        new_2 = ""
        for i in word1:
            new_1 += i
        for j in word2:
            new_2 += j

        return new_1 == new_2
