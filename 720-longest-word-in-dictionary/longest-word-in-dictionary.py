class TrieNode:
    def __init__(self):
        self.children = defaultdict(int)
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        curr = self.root
        for c in word:
            if not curr.children[c]:
                curr.children[c] = TrieNode()

            curr = curr.children[c]
        curr.is_end = True

    def valid(self,word):
        curr = self.root
        for c in word:
            if not curr.children[c]:
                return False
            curr = curr.children[c]

            if not curr.is_end:
                return False
        
        return True

class Solution:
    def longestWord(self, words: List[str]) -> str:

        trie = Trie()
        for i in words:
            trie.insert(i)

        longest = ""

        for w in words:
            if trie.valid(w):
                if len(longest) < len(w):
                    longest = w
                elif len(longest) == len(w):
                    if longest > w:
                        longest = w
                    
        
        return longest


        