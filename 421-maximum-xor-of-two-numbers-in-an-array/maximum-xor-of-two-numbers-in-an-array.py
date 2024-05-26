class TrieNode:
    def __init__(self):
        self.bit = [None, None]

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        temp = self.root
        for i in range(31, -1, -1):
            ch = (num >> i) & 1
            if not temp.bit[ch]:
                temp.bit[ch] = TrieNode()
            temp = temp.bit[ch]

    def find(self, num):
        temp = self.root
        ans = 0
        for i in range(31, -1, -1):
            ch = (num >> i) & 1
            if temp.bit[1 - ch]:
                ans += (1 << i)
                temp = temp.bit[1 - ch]
            else:
                temp = temp.bit[ch]
        return ans

class Solution:
    def findMaximumXOR(self, nums):
        trie = Trie()
        for num in nums:
            trie.insert(num)

        ans = 0
        for num in nums:
            ans = max(ans, trie.find(num))
        
        return ans

