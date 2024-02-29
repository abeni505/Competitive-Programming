# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root , maximum , minimum):
            if not root:
                return True

            if root.val >= maximum or root.val <= minimum:
                return False
            
            return dfs(root.left , root.val , minimum) and dfs(root.right, maximum , root.val)
            

        return dfs(root,float('inf') , float('-inf'))
        



