class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count1 = Counter(word1)
        count2 = Counter(word2)

        val1 = Counter(count1.values())
        val2 = Counter(count2.values())

        # check set difference if they have equal distribution
        # print(val1,val2)
        # print(val1 - val2)

        # print(count1.keys() , count2.keys())
        return len(val1 - val2) == 0 and count1.keys() == count2.keys()
     