class TrieNode():
    def __init__(self):
        self.children = defaultdict(int)
        self.is_end = False

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            if not curr.children[c]:
                curr.children[c] = TrieNode()
            
            curr = curr.children[c]
        curr.is_end = True

    def search(self, word):
        path = []
        curr = self.root
        for c in word:
            if not curr.children[c]:
                return word
            
            path.append(c)

            curr = curr.children[c]

            if curr.is_end:
                return "".join(path)
        
        return word
            

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        trie = Trie()
        for key in dictionary:
            trie.insert(key)
        
        s = sentence.split()

        output = []
        for word in s:
            output.append(trie.search(word))
        
        return " ".join(output)


        

        
        