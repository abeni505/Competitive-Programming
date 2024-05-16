# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
       
        def dfs(root):
            if not root.left and not root.right:
                return root.val
        
            if root.val == 2:
                return dfs(root.left) or dfs(root.right)
            else:
                return dfs(root.left) and dfs(root.right)
            
        return dfs(root)
                