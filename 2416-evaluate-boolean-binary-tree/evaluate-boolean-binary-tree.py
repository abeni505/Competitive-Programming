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
            
            if root.left:
                left = dfs(root.left)
            
            if root.val == 2 and root.right:
                return left or dfs(root.right)
            elif root.val == 3 and root.right:
                return left and dfs(root.right)
                
        return dfs(root)
                