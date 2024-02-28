# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        def dfs(root):
            nonlocal ans
            if not root:
                return 0
            
            ans = max(dfs(root.left) , dfs(root.right)) + 1
            return ans
            
        dfs(root)
        return ans

            
        