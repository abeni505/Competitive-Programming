class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:

        curr = self.root
        for ch in word:
            ind = ord(ch) - ord('a')
            if not curr.children[ind]:
                curr.children[ind] = TrieNode()
            curr = curr.children[ind]
        curr.is_end = True

    def find(self, temp, indx, word):
        if indx == len(word):
            return temp.is_end
            
        if word[indx] == ".":
            for j in range(26):
                if temp.children[j]:
                    if self.find(temp.children[j], indx + 1, word):
                        return True
            
            return False

        ind = ord(word[indx]) - ord('a')
        if not temp.children[ind]:
            return False
            
        return self.find(temp.children[ind], indx + 1, word)

    def search(self, word: str) -> bool:
        return self.find(self.root, 0, word)
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)