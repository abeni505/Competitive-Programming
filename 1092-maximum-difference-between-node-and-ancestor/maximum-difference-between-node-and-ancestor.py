# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root , curr_max , curr_min):
            if not root:
                return curr_max - curr_min
            
            curr_min = min(curr_min , root.val)
            curr_max = max(curr_max , root.val)

            return max(dfs(root.right , curr_max,curr_min) ,
            dfs(root.left, curr_max,curr_min))
        
        return dfs(root,root.val,root.val)