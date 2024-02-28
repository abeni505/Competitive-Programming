# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        

        def mirror(first , second):
            if not first and not second:
                return True
            
            if (not first and second) or (not second and first):
                return False

            if first.val == second.val:
                return mirror(first.left,second.right) and (mirror(first.right , second.left))
        
        
        return mirror(root,root)
