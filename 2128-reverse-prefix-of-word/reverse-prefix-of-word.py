class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word

        left = 0
        right = word.index(ch)

        new = word[left: right + 1][::-1] + word[right + 1:]

        return new