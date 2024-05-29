class TrieNode:
    def __init__(self):
        self.children = defaultdict(int)
        self.count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):

        curr = self.root
        for c in word:
            if not curr.children[c]:
                curr.children[c] = TrieNode()
               
            curr.children[c].count += 1
            curr = curr.children[c]

    
    def search(self, word):

        ans = 0
        curr = self.root
        for c in word: 
            ans += curr.children[c].count
            curr = curr.children[c]
        
        return ans


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        
        trie = Trie()
        for i in words:
            trie.insert(i)


        output = [trie.search(i) for i in words]
        return output


        