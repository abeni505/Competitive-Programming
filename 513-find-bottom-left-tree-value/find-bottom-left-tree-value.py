# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        level = defaultdict(list)

        def dfs(root,lev):
            if not root: return

            level[lev].append(root.val)
            dfs(root.left, lev + 1)
            dfs(root.right, lev + 1)
        
        dfs(root,0)
        
        max_depth = max(level.keys())
    
        return level[max_depth][0]