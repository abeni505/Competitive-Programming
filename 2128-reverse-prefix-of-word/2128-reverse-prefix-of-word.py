class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word: 
            return word

        i = 0
        j=word.index(ch)
        arr = list(word)

        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        
        return "".join(arr)