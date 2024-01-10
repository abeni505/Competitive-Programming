# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
        y = 0
        x = 0
        def dfs(root):
            nonlocal y
            nonlocal x
            if not root:
                return -1 , False
            
            val_left , bool_left = dfs(root.left)
            val_right , bool_right = dfs(root.right)

            if root.val == start:
                
                y = max(val_left , val_right) + 1
                return 0 , True

            if bool_left or bool_right:
                x = max(x , (val_left + val_right) + 2)

            if not bool_left and not bool_right:
                return max(val_left, val_right) + 1 , False
            
            elif bool_left:
                return val_left + 1 ,True
            elif bool_right:
                return val_right + 1 , True

        dfs(root)
        return max(x,y)

        