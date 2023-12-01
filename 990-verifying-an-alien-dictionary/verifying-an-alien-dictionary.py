class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        dict_ = {order[i]: i for i in range(26)}

        for i in range(len(words) - 1):
            for j in range(len(words[i])):

                if j >= len(words[i + 1]) or dict_[words[i][j]] > dict_[words[i + 1][j]]:
                    return False
                elif dict_[words[i][j]] < dict_[words[i + 1][j]]:
                    break

        return True

        