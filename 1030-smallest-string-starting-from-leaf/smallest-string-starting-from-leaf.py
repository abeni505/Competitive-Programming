# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        hashmap = defaultdict(int)
        for i in range(26):
            hashmap[i] = chr(ord("a") + i)

        min_leaf = chr(ord("z") + 1)
        def dfs(node , st):
            nonlocal min_leaf

            if not node: return

            st = hashmap[node.val] + st
            if not node.left and not node.right:
                min_leaf = min(min_leaf , st)
                return
            
            dfs(node.left, st)
            dfs(node.right, st)
        
        dfs(root, "")

        return min_leaf